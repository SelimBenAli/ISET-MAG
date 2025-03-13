from flask import session


class ScannerTools:
    def __init__(self):
        self.scan_endings = ['Enter', 'doubleEnter', 'Tab', 'DownArrow']

    def switch_scan_ending(self, ending_type):
        session['scan_ending'] = ending_type

    def get_scan_ending(self):
        if 'scan_ending' not in session or session['scan_ending'] not in self.scan_endings:
            session['scan_ending'] = 'Enter'
        return session['scan_ending']

    def clear_scan_ending(self):
        session['scan_ending'] = 'Enter'
