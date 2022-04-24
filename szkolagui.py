import random
import UI
import pygame
import pygame_gui as gui


class Szkola:
    def __init__(self, nazwa, wiek, liczba_uczniow, miasto):
        self.nazwa = nazwa
        self.wiek = wiek
        self.liczba_uczniow = liczba_uczniow
        self.miasto = miasto
        self.klasy = []
        print("Stworzono szkołę")

    def uczniowie(self):
        print("Szkoła liczy", self.liczba_uczniow, "uczniów")

    def dodajklase(self, klasa):
        self.klasy.append(klasa)

    def __str__(self):
        return f'Nazwa: {self.nazwa}<br>Wiek: {self.wiek}<br>Liczba uczniów: {self.liczba_uczniow}<br>Miasto: {self.miasto}'


class Klasa:

    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.uczniowie = []

    def oznaczenie(self):
        print(f'Klasa nazywa się {self.nazwa}')

    def zmien(self, nowanazwa):
        self.nazwa = nowanazwa
        print(f'Zmieniono nazwę na {self.nazwa}')

    def __str__(self):
        return f'Klasa {self.nazwa}'

    def dodajucznia(self, uczen):
        self.uczniowie.append(uczen)


class Uczen:
    imie = ""
    nazwisko = ""
    wiek = 0
    grupa = 0
    klasa = ""
    numer = 0

    def __init__(self, imie, nazwisko, wiek, grupa, numer):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
        self.grupa = grupa
        self.numer = numer

    def powiedzcos(self):
        print("Witam jestem", self.imie, self.nazwisko,
              "i jestem w klasie", self.klasa)

    def __str__(self):
        return f'Imię: {self.imie}<br>Nazwisko: {self.nazwisko}<br>Wiek: {self.wiek}<br>Grupa: {self.grupa}<br>Numer: {self.numer}'

    def getfullname(self):
        return f'{self.imie} {self.nazwisko}'


s = Szkola("zsł", 70, 1000, "Gdańsk")
t = Szkola("zse", 10, 200, "Gdańsk")
schoolList = {s.nazwa: s, t.nazwa: t}

imiona = ["Wiktor", "Adrian", "Anna", "Ben", "Rafał", "Ola"]
nazwiska = ["Chleb", "Kowal", "Myszko", "Wiatr", "Oz", "Kłos"]
klasy = {1: "4a", 2: "4b", 3: "4c"}

testowy1 = Uczen(imiona[random.randint(0, 5)], nazwiska[random.randint(
    0, 5)], random.randint(18, 20), random.randint(1, 2), random.randint(1, 100))
testowy2 = Uczen(imiona[random.randint(0, 5)], nazwiska[random.randint(
    0, 5)], random.randint(18, 20), random.randint(1, 2), random.randint(1, 100))
testowy3 = Uczen(imiona[random.randint(0, 5)], nazwiska[random.randint(
    0, 5)], random.randint(18, 20), random.randint(1, 2), random.randint(1, 100))
testowy4 = Uczen(imiona[random.randint(0, 5)], nazwiska[random.randint(
    0, 5)], random.randint(18, 20), random.randint(1, 2), random.randint(1, 100))
testowy5 = Uczen(imiona[random.randint(0, 5)], nazwiska[random.randint(
    0, 5)], random.randint(18, 20), random.randint(1, 2), random.randint(1, 100))
testowy6 = Uczen(imiona[random.randint(0, 5)], nazwiska[random.randint(
    0, 5)], random.randint(18, 20), random.randint(1, 2), random.randint(1, 100))
uczen = Uczen("Adam", "Kowalski", 19, 2, 69)
uczen1 = Uczen("Dariusz", "Kubek", 19, 2, 69)
uczen2 = Uczen("Maria", "Elo", 18, 1, 30)
uczen3 = Uczen("Emilia", "Psychasiada", 17, 1, 25)
uczen4 = Uczen("Władysław", "Bąk", 20, 1, 12)

k = Klasa("4a")
k2 = Klasa("4b")
k3 = Klasa("4c")
tk = Klasa("4a")
tk2 = Klasa("4b")
tk3 = Klasa("4c")

k.dodajucznia(testowy1)
k.dodajucznia(uczen)
k.dodajucznia(uczen1)
k2.dodajucznia(uczen2)
k2.dodajucznia(uczen3)
k2.dodajucznia(testowy2)
s.dodajklase(k)
s.dodajklase(k2)
s.dodajklase(k3)
tk.dodajucznia(testowy2)
tk.dodajucznia(testowy4)
tk2.dodajucznia(testowy3)
tk2.dodajucznia(testowy5)
tk3.dodajucznia(testowy1)
tk3.dodajucznia(testowy6)
t.dodajklase(tk)
t.dodajklase(tk2)
t.dodajklase(tk3)


class Window:
    window_size = [1000, 900]
    clock = None
    manager = None
    screen = None
    background_color = (25, 25, 25)
    running = True

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Szkoły')
        self.screen = pygame.display.set_mode(self.window_size)
        self.screen.fill(self.background_color)
        pygame.display.flip()
        self.manager = gui.UIManager(
            (self.window_size[0], self.window_size[1]))
        self.schoolList = schoolList
        self.listC = {}
        self.listS = {}
        self.coordinates = []
        self.AddStudentNames = ["Imię", "Nazwisko", "Wiek", "Grupa", "Numer"]
        self.AddSchoolNames = ["Nazwa", "Wiek", "Liczba uczniów", "Miasto"]

    def update(self):
        while self.running:
            time_delta = self.clock.tick(60) / 1000.0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    import sys
                    sys.exit()
                if event.type == pygame.USEREVENT:
                    if event.user_type == gui.UI_SELECTION_LIST_NEW_SELECTION:
                        if event.ui_element == UI.SchoolList:

                            self.listC = {
                                c.nazwa: c for c in self.schoolList[event.text].klasy}
                            UI.ClassList.set_item_list(self.listC)
                            UI.ClassList.show()
                        if event.ui_element == UI.ClassList:
                            self.listS = {
                                s.getfullname(): s for s in self.listC[event.text].uczniowie}
                            UI.StudentList.set_item_list(self.listS)
                            UI.StudentList.show()
                        if event.ui_element == UI.StudentList:
                            UI.StudentInfo.html_text = str(
                                self.listS[event.text])
                            UI.StudentInfo.rebuild()
                            UI.StudentInfo.show()

                    if event.user_type == gui.UI_BUTTON_PRESSED:
                        if event.ui_element == UI.DeleteSchool:
                            if UI.SchoolList.get_single_selection():
                                del schoolList[UI.SchoolList.get_single_selection()]
                                UI.SchoolList.set_item_list(schoolList)
                                UI.ClassList.hide()
                                UI.StudentList.hide()
                                UI.StudentInfo.hide()
                                UI.SchoolInfo.hide()

                        if event.ui_element == UI.DeleteClass:
                            if UI.ClassList.get_single_selection():
                                self.schoolList[UI.SchoolList.get_single_selection()].klasy.remove(
                                    self.listC[UI.ClassList.get_single_selection()])
                                del self.listC[UI.ClassList.get_single_selection()]

                                UI.ClassList.set_item_list(self.listC)
                                UI.StudentList.hide()
                                UI.StudentInfo.hide()

                        if event.ui_element == UI.DeleteStudent:
                            if UI.StudentList.get_single_selection():
                                if self.listC[UI.ClassList.get_single_selection()]:
                                    self.listC[UI.ClassList.get_single_selection()].uczniowie.remove(
                                        self.listS[UI.StudentList.get_single_selection()])
                                    del self.listS[UI.StudentList.get_single_selection(
                                    )]

                                UI.StudentList.set_item_list(self.listS)
                                UI.StudentInfo.hide()

                        if event.ui_element == UI.SchoolInfoBtn:
                            if UI.SchoolList.get_single_selection():
                                UI.SchoolInfo.html_text = str(
                                    schoolList[UI.SchoolList.get_single_selection()])

                                UI.SchoolInfo.rebuild()
                                UI.SchoolInfo.show()
                                UI.HideSchool.show()

                        if event.ui_element == UI.HideSchool:
                            UI.SchoolInfo.rebuild()
                            UI.HideSchool.hide()
                            UI.SchoolInfo.hide()

                        if event.ui_element == UI.AddClass:
                            UI.AddClassForm.show()

                        if event.ui_element == UI.AddStudent:
                            UI.AddStudentForm.show()

                        if event.ui_element == UI.AddStudentAddBtn:
                            klasa = UI.ClassList.get_single_selection()
                            self.listC[klasa].dodajucznia(
                                Uczen(*[value.text for value in UI.AddStudentInput]))
                            self.listS = {
                                s.getfullname(): s for s in self.listC[klasa].uczniowie}
                            UI.StudentList.set_item_list(self.listS)
                            UI.AddStudentForm.hide()

                        if event.ui_element == UI.AddSchool:
                            UI.AddSchoolForm.show()

                        if event.ui_element == UI.AddSchoolHideBtn:
                            UI.AddSchoolForm.hide()

                        if event.ui_element == UI.AddSchoolAddBtn:
                            szkola = Szkola(
                                *[value.text for value in UI.AddSchoolInput])
                            self.schoolList[szkola.nazwa] = szkola
                            UI.SchoolList.set_item_list(self.schoolList)
                            UI.AddSchoolForm.hide()

                        if event.ui_element == UI.AddClassHide:
                            UI.AddClassForm.hide()

                        if event.ui_element == UI.AddClassAddBtn:
                            nazwa = UI.AddClassText1.get_text()
                            self.schoolList[UI.SchoolList.get_single_selection()].klasy.append(
                                Klasa(nazwa))
                            UI.ClassList.set_item_list(self.listC)
                            UI.ClassList.rebuild()
                            UI.ClassList.hide()
                            UI.AddClassForm.hide()

                        if event.ui_element == UI.AddStudentHideBtn:
                            UI.AddStudentForm.hide()

                if event.type == pygame.MOUSEMOTION:
                    self.coordinates = list(pygame.mouse.get_pos())
                    UI.Counter.html_text = f'X:{self.coordinates[0]} Y:{self.coordinates[1]}'
                    UI.Counter.rebuild()

                self.manager.process_events(event)

            self.screen.fill(self.background_color)
            self.manager.update(time_delta)
            self.screen.blit(self.screen, (0, 0))
            self.manager.draw_ui(self.screen)
            pygame.display.update()

    def LoadUI(self):
        UI.SchoolList = gui.elements.UISelectionList(manager=self.manager, relative_rect=pygame.Rect(
            (30, 0), (300, 200)), item_list=schoolList)
        UI.ClassList = gui.elements.UISelectionList(manager=self.manager, relative_rect=pygame.Rect(
            (350, 0), (300, 200)), item_list=[])
        UI.StudentList = gui.elements.UISelectionList(manager=self.manager, relative_rect=pygame.Rect(
            (660, 0), (300, 200)), item_list=[])
        UI.StudentInfo = gui.elements.UITextBox(manager=self.manager, relative_rect=pygame.Rect(
            (660, 210), (300, 200)), html_text="")

        # Usuwanie
        UI.DeleteSchool = gui.elements.UIButton(manager=self.manager, relative_rect=pygame.Rect(
            (30, 300), (100, 50)), text="Usuń szkołę", tool_tip_text="Usuwa szkolę")
        UI.DeleteClass = gui.elements.UIButton(manager=self.manager, relative_rect=pygame.Rect(
            (160, 300), (100, 50)), text="Usuń klasę", tool_tip_text="Usuwa klasę")
        UI.DeleteStudent = gui.elements.UIButton(manager=self.manager, relative_rect=pygame.Rect(
            (290, 300), (100, 50)), text="Usuń ucznia", tool_tip_text="Usuwa ucznia")

        # Informacje o szkole
        UI.SchoolInfo = gui.elements.UITextBox(manager=self.manager, relative_rect=pygame.Rect(
            (30, 400), (200, 100)), html_text="", layer_starting_height=1)
        UI.SchoolInfoBtn = gui.elements.UIButton(manager=self.manager, relative_rect=pygame.Rect(
            (30, 350), (100, 50)), text="Pokaż szkołę", tool_tip_text="Pokazuje informacje o szkole")
        UI.HideSchool = gui.elements.UIButton(manager=self.manager, relative_rect=pygame.Rect(
            (80, 500), (100, 50)), text="Schowaj", starting_height=1)

        # Koordynaty
        UI.Counter = gui.elements.UITextBox(manager=self.manager, relative_rect=pygame.Rect(
            (890, 850), (110, 50)), html_text="")

        # Dodawawanie klasy
        UI.AddClass = gui.elements.UIButton(manager=self.manager, relative_rect=pygame.Rect(
            (420, 300), (100, 50)), text="Dodaj klasę", tool_tip_text="Dodaje klasę")
        UI.AddClassForm = gui.elements.UIPanel(manager=self.manager, relative_rect=pygame.Rect(
            (420, 370), (200, 100)), starting_layer_height=0)
        UI.AddClassText1 = gui.elements.UITextEntryLine(
            manager=self.manager, relative_rect=pygame.Rect((60, 15), (100, 50)), container=UI.AddClassForm)
        UI.AddClassName = gui.elements.UILabel(manager=self.manager, relative_rect=pygame.Rect(
            (0, 0), (60, 60)), text="Nazwa: ", container=UI.AddClassForm)
        UI.AddClassHide = gui.elements.UIButton(manager=self.manager, relative_rect=pygame.Rect(
            (110, 60), (75, 25)), text="Schowaj", container=UI.AddClassForm)
        UI.AddClassAddBtn = gui.elements.UIButton(manager=self.manager, relative_rect=pygame.Rect(
            (10, 60), (75, 25)), text="Dodaj", container=UI.AddClassForm)

        # Dodawanie ucznia
        UI.AddStudent = gui.elements.UIButton(manager=self.manager, relative_rect=pygame.Rect(
            (30, 550), (100, 50)), text="Dodaj ucznia", tool_tip_text="Dodaje ucznia")
        UI.AddStudentForm = gui.elements.UIPanel(manager=self.manager, relative_rect=pygame.Rect(
            (30, 600), (250, 250)), starting_layer_height=10, visible=False)

        for i, name in enumerate(self.AddStudentNames):
            UI.AddStudentText.append(gui.elements.UILabel(manager=self.manager, relative_rect=pygame.Rect(
                (0, i*30), (100, 30)), text=f'{name}: ', container=UI.AddStudentForm))
            UI.AddStudentInput.append(gui.elements.UITextEntryLine(
                manager=self.manager, relative_rect=pygame.Rect((100, i*30), (100, 30)), container=UI.AddStudentForm))

        UI.AddStudentAddBtn = gui.elements.UIButton(manager=self.manager, relative_rect=pygame.Rect(
            (30, 175), (75, 25)), text="Dodaj", container=UI.AddStudentForm)
        UI.AddStudentHideBtn = gui.elements.UIButton(manager=self.manager, relative_rect=pygame.Rect(
            (130, 175), (75, 25)), text="Schowaj", container=UI.AddStudentForm)

        # Dodawanie szkoły
        UI.AddSchool = gui.elements.UIButton(manager=self.manager, relative_rect=pygame.Rect(
            (500, 550), (100, 50)), text="Dodaj szkołę", tool_tip_text="Dodaje szkołę")
        UI.AddSchoolForm = gui.elements.UIPanel(manager=self.manager, relative_rect=pygame.Rect(
            (400, 600), (300, 200)), starting_layer_height=10, visible=False)

        for i, name in enumerate(self.AddSchoolNames):
            UI.AddSchoolText.append(gui.elements.UILabel(manager=self.manager, relative_rect=pygame.Rect(
                (0, i*30), (150, 30)), text=f'{name}: ', container=UI.AddSchoolForm))
            UI.AddSchoolInput.append(gui.elements.UITextEntryLine(
                manager=self.manager, relative_rect=pygame.Rect((150, i*30), (100, 30)), container=UI.AddSchoolForm))

        UI.AddSchoolAddBtn = gui.elements.UIButton(manager=self.manager, relative_rect=pygame.Rect(
            (50, 150), (75, 25)), text="Dodaj", container=UI.AddSchoolForm)
        UI.AddSchoolHideBtn = gui.elements.UIButton(manager=self.manager, relative_rect=pygame.Rect(
            (150, 150), (75, 25)), text="Schowaj", container=UI.AddSchoolForm)

        UI.ClassList.hide()
        UI.StudentList.hide()
        UI.StudentInfo.hide()
        UI.SchoolInfo.hide()
        UI.HideSchool.hide()
        UI.AddClassForm.hide()


w = Window()
w.LoadUI()
w.update()
