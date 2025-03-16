class HardwareTools:
    def __init__(self):
        ...

    def generate_code_barre_hardware(self, code):
        ch = ''
        for i in code:
            if "A" <= i <= "Z" or "a" <= i <= "z":
                ch += str(ord(i.lower()))
            else:
                ch += str(i)
        while len(ch) < 12:
            ch = '0' + ch
        ch = '7' + ch
        print("code a barre : ", code, " => ", ch)
        return ch

    def check_num_inventaire(self, num_inventaire):
        if num_inventaire is None or num_inventaire == '':
            return False
        if not num_inventaire.isdigit():
            return False
        return True
