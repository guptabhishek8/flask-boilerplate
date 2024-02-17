"""Data-wrangling for loggers"""
import arrow
import json
import logging
import connexion
import pytz
from flask import g
import traceback

# from settings import ENV, DEBUG

class ContextualFilter(logging.Filter):
    """
        Overrides loggging.Filter Class to append the UUID 
        to the logging Context. DOES NOT FILTER ANY LOGS, all logs are passed.
    """
    def filter(self, log_record):
        """Filter messages to be logged.

        Parameters
        ----------
        `log_record` : <logging.LogRecord>
            The log-record to be processed and filtered.

        Returns
        -------
        `True`
            if the `log_record` is to be logged.
        `False`
            if the `log_record` is to be dropped.

        Notes
        -----
        Currently we aren't dropping any logs. This function simply transforms
        the log-record by injecting additional data into it, and prepares keys
        for the log-formatter.
        """

        def _get_trace():
            trace = ""
            if log_record.levelname in ['ERROR', 'CRITICAL']:
                trace = traceback.format_exc().strip() # Get the recent stack-trace

            return json.dumps(trace)

        def _get_msg():
            msg = log_record.msg
            try:
                # `loads` and `dumps` for printing JSON structure in a single line
                json_data = json.loads(log_record.msg)
                msg = json.dumps(json_data)

            except json.decoder.JSONDecodeError:
                msg = json.dumps({
                    "TEXT": log_record.msg,
                })
            except TypeError:
                # We tried to `json.loads` something that's not a string
                # Let's print its string-representation
                msg = json.dumps({
                    "OBJ": repr(log_record.msg),
                })
            return msg

        def _get_rayid():
            try:
                if hasattr(g, 'SYNS_RAY_ID'):
                    return g.SYNS_RAY_ID
            except RuntimeError: # if you're running outside of a Flask app-context
                pass
            return ""

        def _get_loan_ref_id():
            try:
                if connexion.request.view_args:
                    loan_ref_id = connexion.request.view_args.get('loan_application_no')
                    if loan_ref_id is None:
                        return _get_from_global('LOAN_REF_ID')
                    else:
                        return loan_ref_id
            except RuntimeError:
                # We're running outside of the Flask app context
                pass
            return _get_from_global('LOAN_REF_ID')

        def _get_from_global(attr_name):
            try:
                if hasattr(g, attr_name):
                    return getattr(g, attr_name) or ""
            except RuntimeError: # if you're running outside of a Flask app-context
                pass
            return ""

        def _get_log_time():
            tz_IST = pytz.timezone(pytz.country_timezones['IN'][0])
            return str(arrow.now(tz=tz_IST).format('YYYY-MM-DDTHH:mm:ss.SSSZZ'))

        log_record.trace = _get_trace()
        log_record.msg = _get_msg()
        log_record.ray_id = _get_rayid()
        log_record.loan_ref_id = _get_loan_ref_id()
        log_record.error_code = _get_from_global('ERROR_CODE')
        log_record.pan = _get_from_global('PAN')
        log_record.msisdn = _get_from_global('MSISDN')
        log_record.time = _get_log_time()

        return True # Don't drop any logs


class ContextHandler(logging.StreamHandler):
    """
        Overrides logging.StreamHandler to append the MSISDN, PAN etc.
        to the logging Context
    """
    def __init__(self, *args, **kwargs):
        logging.StreamHandler.__init__(self, *args, **kwargs)
        self.addFilter(ContextualFilter())
