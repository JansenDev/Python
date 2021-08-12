import re


class Utilidades():
    __wordsDictionary: dict = {}
    __vocalDictionary: dict = {}

    def __init__(self, cadena: str = None, entero: int = None):
        self.__cadena = cadena
        self.__entero = entero

    def __str__(self):
        return "Cadena:{0}\nEntero: {1}".format(self.__cadena, self.__entero)

    def textReverse(self, texto: str = None) -> str:
        self.__cadena: str = texto if texto else self.__cadena
        textReversed: str = ''
        textLength: int = len(self.__cadena)
        # *Forma 1
        # for word in self.__cadena:
        #     textReversed = word + textReversed

        # *forma 2
        for wordIndex in range(0, textLength):
            textReversed = self.__cadena[wordIndex] + textReversed

        return textReversed

    def decimalToBinary(self, decimal: int = None) -> int:
        self.__entero = decimal if decimal else self.__entero
        binaryResult: str = ''
        dividendo: int = self.__entero
        resto: int = None

        while(dividendo > 0):
            resto = str(dividendo - (int(dividendo/2)*2))
            dividendo = int(dividendo/2)

            binaryResult = resto + binaryResult
        return int(binaryResult)

    def binaryToDecimal(self, binary: int = None) -> int:
        self.__entero = binary if binary else self.__entero
        binaryStr: str = str(self.__entero)

        potencia: int = 0
        decimalResult: int = 0
        binaryLength: int = len(binaryStr)

        for num in range(binaryLength-1, -1, -1):
            decimalResultAux = int(binaryStr[num])*(2**potencia)
            decimalResult += decimalResultAux
            potencia += 1

        return decimalResult

    def decimalToHexadecimal(self, decimal: int = None) -> str:
        self.__entero = decimal if decimal else self.__entero
        dividendo: int = self.__entero
        resto: int = None
        hexadecimalResult: str = ''

        while(dividendo > 0):
            resto = dividendo - (int(dividendo/16)*16)
            dividendo = int(dividendo/16)

            if (resto == 10):
                resto = "A"
            elif (resto == 11):
                resto = "B"
            elif (resto == 12):
                resto = "C"
            elif (resto == 13):
                resto = "D"
            elif (resto == 14):
                resto = "E"
            elif (resto == 15):
                resto = "F"

            hexadecimalResult = str(resto) + hexadecimalResult
        return hexadecimalResult

    def hexadecimalToDecimal(self, hexadecimal: str = None) -> int:
        self.__cadena = hexadecimal if hexadecimal else self.__cadena
        hexadecimalLength: int = len(self.__cadena)
        cadenaAux = self.__cadena
        decimalResult: int = 0
        hexaUnit: int = None
        potencia: int = 0

        for hexa in range(hexadecimalLength-1, -1, -1):
            hexaUnit = cadenaAux[hexa]
            if (hexaUnit == "A"):
                hexaUnit = 10
            elif (hexaUnit == "B"):
                hexaUnit = 11
            elif (hexaUnit == "C"):
                hexaUnit = 12
            elif (hexaUnit == "D"):
                hexaUnit = 13
            elif (hexaUnit == "E"):
                hexaUnit = 14
            elif (hexaUnit == "F"):
                hexaUnit = 15

            decimalResultAux: int = int(hexaUnit) * (16**potencia)
            decimalResult += decimalResultAux
            potencia += 1

        return decimalResult

    def decimalToBase(self, decimal: int = None, base: int = 10) -> str:
        self.__entero = decimal if decimal else self.__entero
        baseResult: str = ""
        dividendo: int = self.__entero
        resto: int = None

        if(base == 16):
            return self.decimalToHexadecimal(dividendo)

        while(dividendo > 0):
            resto = str(dividendo - int(dividendo/base)*base)
            dividendo = int(dividendo/base)
            baseResult = resto + baseResult

        return baseResult

    def baseToDecimal(self, number: str = None, inBase: int = None) -> str:
        self.__cadena = number if number else self.__cadena
        potencia: int = 0
        baseResult: int = 0
        numberStr = str(self.__cadena)
        numberLength: int = len(numberStr)

        if(inBase == 16):
            return self.hexadecimalToDecimal(number)

        for num in range(numberLength-1, -1, -1):
            baseResultAux = int(numberStr[num]) * (inBase**potencia)
            baseResult = baseResultAux + baseResult
            potencia += 1
            print(baseResultAux)

        return baseResult

    def isEmail(self, string: str = None) -> bool:
        self.__cadena = string if string else self.__cadena
        regex: str = r"(^[a-zA-Z0-9\_\.\-]+)(@{1})([a-z0-9]+)(\.[a-z0-9]*)?(\.[a-z0-9]*)"
        isEmailResult: bool = False

        if(string == "" or string == " " or len(string) == 0):
            return False

        try:
            stringFound = re.fullmatch(regex, self.__cadena)

            if(stringFound.group()):
                isEmailResult = True
        except:
            isEmailResult = False

        return isEmailResult

    def isPhone(self, string: str = None) -> str:
        self.__cadena = string if string else self.__cadena
        regex: str = r"^(\+(\d{2}|\d{3})\s?)?(\d{3}|\(\d{3}\))(\-|\s)?((\d{3})(\-|\s)?(\d{3})|(\d{2})(\-|\s)?(\d{4}))"
        isPhoneResult: bool = False

        if(string == "" or string == " " or len(string) == 0):
            return False

        try:
            stringFound = re.fullmatch(regex, self.__cadena)

            if(stringFound.group()):
                isPhoneResult = True
        except:
            return False

        return isPhoneResult

    def isUpperCase(self, word: str = None) -> bool:
        regex: str = r"[A-Z]"
        try:
            match = re.search(regex, word)
            if(match.group()):
                return True
        except:
            return False

    def countUpperCase(self, string: str = None) -> str:
        self.__cadena = string if string else self.__cadena
        stringLength: int = len(self.__cadena)
        upperCount: int = 0

        for index in range(stringLength):

            if self.isUpperCase(self.__cadena[index]):
                upperCount += 1

        return upperCount

    def countVocal(self, string: str = None) -> str:
        self.__cadena = string if string else self.cadena
        vocalesList: list = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        countVocales: int = 0

        for word in string:
            if word in vocalesList:
                countVocales += 1

        return countVocales

    def countWords(self, string: str = None) -> dict:
        self.__cadena = string if string else self.cadena
        regex:str=r"[A-Za-z]+"

        wordList = re.findall(regex, string)
        
        for word in wordList:
            wordFormated:str = word.lower()
            self._saveWordInDictionary(wordFormated, self.__wordsDictionary)

        return self.__wordsDictionary

    def vocalCount(self, string:str=None)->dict:
        self.__cadena = string if string else self.__cadena
        regex: str = r"[AEIOUaeiou]"

        vocalList = re.findall(regex, string)

        for vocal in vocalList:
            vocalFormated:str = vocal.lower()
            self._saveWordInDictionary(vocalFormated, self.__vocalDictionary)

        return self.__vocalDictionary

    def _saveWordInDictionary(self, string: str = None, dictionary:dict=None):

        try:
            if string in dictionary:
                count: int = dictionary.get(string)
                dictionary[string] = count+1
            else:
                dictionary[string] = 1
        except:
            print("Error saveWordInDictionary")


# ?Hacer un algoritmo que determine si es o no un correo electronico es válido/
# ?Hacer un algoritmo que determine si es o no un N° telefono es válido/
# ?contar vocales de un string/
# ?contar cuantas veces se recipite las vocales de un string/
# ?contar cuantas veces se recipite las palabras de un string /
# ?ver si existen mayusculas|


variable = Utilidades()
s = variable.binaryToDecimal("0111")
s2 = variable.decimalToBinary(25)
s3 = variable.decimalToHexadecimal(2500)
s4 = variable.hexadecimalToDecimal("4F7A")
s5 = variable.decimalToBase(250, base=16)
s6 = variable.baseToDecimal("FA", inBase=16)

email: str = "seguragjj@gmail.com"
email2: str = "seguragjj25@gmail.com"
email3: str = "segura_galindo.snk25@hotmail.n4t.net"
emailInvalid: str = "segura_gal indo.snk25@hotmail@n4t.net"
emailInvalid2: str = "segura_gal indo.snk25@hotmail@n4t.net segura_galindo.snk25@hotmail.n4t.net seguragjj@gmail.com"
emailNull = " "
emailNull2 = "segura_gali ndo.snk25@hotmail.n4t.net"
s7 = variable.isEmail(email3)

phone: str = "900740609"
phone2: str = "900-740-609"
phone3: str = "(900)740609"
phoneExt: str = "822-891859"
phoneExt2: str = "130-88-9422"
phoneExt3: str = "13088-9422"
phone4: str = "+51 900740609"
phone5: str = "(900) 740-609"
phone6: str = "900 740 009"
phoneInvalid: str = "+51 9a0740609"
phoneInvalid2: str = "+512 90074060995"
phoneInvalid3: str = "+512 90074060995"
phoneNull: str = " "


s8 = variable.isPhone(phoneExt2)
# s9=variable.isUpperCase("S")##Test

stringTest: str = "Hola mundo como estas aqui prObando coMo dev oooo.ii"
s10 = variable.countUpperCase(stringTest)
s11 = variable.countVocal(stringTest)
s12 = variable.countWords(stringTest)
s13 = variable.vocalCount(stringTest)



print(s13)
# print(variable)
# print(s6)
# print(s)
# print(s2)
