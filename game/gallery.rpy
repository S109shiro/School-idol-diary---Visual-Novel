init python:
    gallery_honoka = Gallery()
    gallery_honoka.transition = fade

    gallery_honoka.button("Test_Honoka1")
    gallery_honoka.unlock_image("H11")


    gallery_honoka.button("Test Honoka2")
    gallery_honoka.unlock_image("H12")


    gallery_honoka.button("Test Honoka3")
    gallery_honoka.unlock_image("H13")



    gallery_honoka.button("Test Honoka4")
    gallery_honoka.unlock_image("H14")


    gallery_honoka.button("Test Honoka5")
    gallery_honoka.unlock_image("H15")


    gallery_honoka.button("Test Honoka6")
    gallery_honoka.unlock_image("H16")


    gallery_honoka.button("Test Honoka7")
    gallery_honoka.unlock_image("H17")

    gallery_honoka.button("Test Honoka8")
    gallery_honoka.unlock_image("H18")

screen gallery():
    tag menu
    add "backgroundG"
    default page = 1
        
        
    hbox:
        xalign 0.5
        yalign 1.0
        textbutton "Pagina 1" action SetScreenVariable("page", 1)
        textbutton "Pagina 2" action SetScreenVariable("page", 2)
        textbutton "Pagina 3" action SetScreenVariable("page", 3)
        textbutton "Pagina 4" action SetScreenVariable("page", 4)
        textbutton "Pagina 5" action SetScreenVariable("page", 5)

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 20
        if page == 1:
            text "CAPITULO 1 - HONOKA NO SE RENDIRÁ"
            grid 3 3:
                spacing 10
                vbox:  
                    add gallery_honoka.make_button(name = "Test_Honoka1", locked = "blockH", unlocked = "H11")
                vbox:  
                    add gallery_honoka.make_button(name = "Test Honoka2", locked = "blockH", unlocked = "H12")
                vbox:  
                    add gallery_honoka.make_button(name = "Test Honoka3", locked = "blockH", unlocked = "H13")
                vbox:  
                    add gallery_honoka.make_button(name = "Test Honoka4", locked = "blockH", unlocked = "H14")
                vbox:  
                    add gallery_honoka.make_button(name = "Test Honoka5", locked = "blockH", unlocked = "H15")
                vbox:  
                    add gallery_honoka.make_button(name = "Test Honoka6", locked = "blockH", unlocked = "H16")
                vbox:  
                    add gallery_honoka.make_button(name = "Test Honoka7", locked = "blockH", unlocked = "H17")
                vbox:  
                    add gallery_honoka.make_button(name = "Test Honoka8", locked = "blockH", unlocked = "H18")
        if page == 2:
            text "CAPITULO 2 - CONVIRTÁMONOS EN SCHOOL IDOLS"
            grid 3 3:
                spacing 10
                vbox:  
                    add gallery_honoka.make_button(name = "Test_Honoka1", locked = "blockH", unlocked = "H21")
                vbox: 
                    add gallery_honoka.make_button(name = "Test Honoka2", locked = "blockH", unlocked = "H22")
                vbox: 
                    add gallery_honoka.make_button(name = "Test Honoka3", locked = "blockH", unlocked = "H23")
                vbox: 
                    add gallery_honoka.make_button(name = "Test Honoka4", locked = "blockH", unlocked = "H24")
                vbox: 
                    add gallery_honoka.make_button(name = "Test Honoka5", locked = "blockH", unlocked = "H25")
                vbox: 
                    add gallery_honoka.make_button(name = "Test Honoka6", locked = "blockH", unlocked = "H26")
                vbox: 
                    add gallery_honoka.make_button(name = "Test Honoka7", locked = "blockH", unlocked = "H27")
                vbox: 
                    add gallery_honoka.make_button(name = "Test Honoka8", locked = "blockH", unlocked = "H28")
        if page == 3:
            text "CAPITULO 3 - ¡BAILEMOS!"
            grid 3 3:
                spacing 10
                vbox:  
                    add gallery_honoka.make_button(name = "Test_Honoka1", locked = "blockH", unlocked = "H31")
                vbox: 
                    add gallery_honoka.make_button(name = "Test Honoka2", locked = "blockH", unlocked = "H32")
                vbox: 
                    add gallery_honoka.make_button(name = "Test Honoka3", locked = "blockH", unlocked = "H33")
                vbox: 
                    add gallery_honoka.make_button(name = "Test Honoka4", locked = "blockH", unlocked = "H34")
                vbox: 
                    add gallery_honoka.make_button(name = "Test Honoka5", locked = "blockH", unlocked = "H35")
                vbox: 
                    add gallery_honoka.make_button(name = "Test Honoka6", locked = "blockH", unlocked = "H36")
                vbox: 
                    add gallery_honoka.make_button(name = "Test Honoka7", locked = "blockH", unlocked = "H37")
                vbox: 
                    add gallery_honoka.make_button(name = "Test Honoka8", locked = "blockH", unlocked = "H38")
        if page == 4:
            text "CAPITULO 4 - QUIERO UN SALÓN PROPIO"
            grid 3 3:
                spacing 10
                vbox:  
                    add gallery_honoka.make_button(name = "Test_Honoka1", locked = "blockH", unlocked = "H31")
                vbox: 
                    add gallery_honoka.make_button(name = "Test Honoka2", locked = "blockH", unlocked = "H32")
                vbox: 
                    add gallery_honoka.make_button(name = "Test Honoka3", locked = "blockH", unlocked = "H33")
                vbox: 
                    add gallery_honoka.make_button(name = "Test Honoka4", locked = "blockH", unlocked = "H34")
                vbox: 
                    add gallery_honoka.make_button(name = "Test Honoka5", locked = "blockH", unlocked = "H35")
                vbox: 
                    add gallery_honoka.make_button(name = "Test Honoka6", locked = "blockH", unlocked = "H36")
                vbox: 
                    add gallery_honoka.make_button(name = "Test Honoka7", locked = "blockH", unlocked = "H37")
                vbox: 
                    add gallery_honoka.make_button(name = "Test Honoka8", locked = "blockH", unlocked = "H38")

    hbox:
        xalign 0.02
        yalign 1.0
        textbutton _("Volver") action Return()