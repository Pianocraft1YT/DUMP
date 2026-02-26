#History project code

import turtle as trtl

wn = trtl.Screen() 
Title_font = ("Arial", 50, "normal")
header_font = ("Arial", 40, "normal")
subtile_font = ("Arial", 20, "normal")
paragraph_font = ("Arial", 15, "normal")
source_font = ("Arial", 12, "normal")
orange_state_flag = ("orange_state_flag.gif")
coin = "coin.gif"
cross = "cross.gif"
leaf = "leaf.gif"
gun = "military.gif"
apple = "apple.gif"
pyrmid = "social_pyrimid.gif"
brain = "brain.gif"
brit_flag = "british_flag.gif"
south_african_flag = "south_african_flag.gif"
timeline = "timeline.gif"
book = "book.gif"
claim = "claim.gif"
transval_flag = "transval_flag.gif"
political = "Political.gif"
economy = "economy.gif"
religous = "religous.gif"
social = "social.gif"
envrioment = "enviroment.gif"
education = "education.gif"
government = "government.gif"
burden = "burden.gif"
wn.addshape(coin)
wn.addshape(cross)
wn.addshape(leaf)
wn.addshape(gun)
wn.addshape(pyrmid)
wn.addshape(apple)
wn.addshape(brain)
wn.addshape(brit_flag)
wn.addshape(south_african_flag)
wn.addshape(timeline)
wn.addshape(book)
wn.addshape(claim)
wn.addshape(orange_state_flag)
wn.addshape(transval_flag)
wn.addshape(political)
wn.addshape(economy)
wn.addshape(religous)
wn.addshape(education)
wn.addshape(social)
wn.addshape(envrioment)
wn.addshape(government)
wn.addshape(burden)

def home_page(x,y):
 wn.clear()
 global button_1,button_2,button_3,button_4,button_5,button_6,button_7,button_8,button_9,button_10,button_11,printer
 wn.bgcolor("maroon")
 button_1 = trtl.Turtle()
 button_2 = trtl.Turtle()
 button_3 = trtl.Turtle()
 button_4 = trtl.Turtle()
 button_5 = trtl.Turtle()
 button_6 = trtl.Turtle()
 button_7 = trtl.Turtle()
 button_8 = trtl.Turtle()
 button_9 = trtl.Turtle()
 button_10 = trtl.Turtle()
 button_11 = trtl.Turtle()
 button_12 = trtl.Turtle()
 printer = trtl.Turtle()
 wn.tracer(0,0)
 printer.penup()
 printer.hideturtle()
 printer.setposition(-500, 300)
 printer.color("White")
 printer.write("British Imperialism in South Africa", font=Title_font)
 printer.setposition(-250, 250)
 printer.write("By Malcolm McNeill and Lucca Chen", font=subtile_font)
 printer.setposition(-625,-350)
 printer.write("Click on the ", font=header_font)
 printer.setposition(275, -350)
 printer.write("images to learn!",font=header_font)
 buttons = [button_1,button_2,button_3,button_4,button_5,button_6,button_7,button_8,button_9,button_10,button_11,button_12]
 for button in buttons:
  button.penup()
 button_1.setposition(-525, 100)
 button_2.setposition(-525, -100)
 button_3.setposition(-275, 100)
 button_4.setposition(-275, -100)
 button_5.setposition(-25, 100)
 button_6.setposition(-25, -100)
 button_7.setposition(225, 100)
 button_8.setposition(250, -100)
 button_9.setposition(475, 100)
 button_10.setposition(475, -100)
 button_11.setposition(150, -300)
 button_12.setposition(-125, -300)
 button_5.shape(coin)
 button_7.shape(cross)
 button_6.shape(leaf)
 button_11.shapesize(5)
 button_11.shape("circle")
 button_8.shape(gun)
 button_10.shape(apple)
 button_9.shape(pyrmid)
 button_2.shape(brain)
 button_4.shape(brit_flag)
 button_12.shape(south_african_flag)
 button_1.shape(book)
 button_3.shape(timeline)
 wn.update()
 button_1.onclick(get_page)
 button_2.onclick(get_page)
 button_3.onclick(get_page)
 button_4.onclick(get_page)
 button_5.onclick(get_page)
 button_6.onclick(get_page)
 button_7.onclick(get_page)
 button_8.onclick(get_page)
 button_9.onclick(get_page)
 button_10.onclick(get_page)
 button_11.onclick(get_page)
 button_12.onclick(get_page)

def get_page(x,y):
  if y > 0:
    if x > -600 and x < -450:
        page = 1
    elif x > -370 and x < -185 :
        page = 2
    elif x > -110 and x < 60:
        page = 3
    elif x > 165 and x < 280 :
        page = 4
    elif x > 350 and x < 600:
        page = 5
  elif y < 0 and y > -200:
    if x > -600 and x < -450:
        page = 6
    elif x > -400 and x < -160 :
        page = 7
    elif x > -130 and x < 80:
        page = 8
    elif x > 170 and x < 330 :
        page = 9
    elif x > 400 and x < 550:
        page = 10
  elif y < -200:
      if x < 0:
        page = 11
      elif x > 0:
        page = 12
  else:
    printer.clear()
    printer.write("Error", font=Title_font)
  make_page(page)
def make_page(page):
    global button_home
    wn.clear()
    wn.bgcolor("maroon")
    button_home = trtl.Turtle()
    wn.tracer(0,0)
    button_home.shapesize(10)
    button_home.penup()
    button_home.setposition(-700, 350)
    button_home.right(180)
    printer_2 = trtl.Turtle()
    printer_2.penup()
    printer_2.hideturtle()
    image_stamp = trtl.Turtle()
    image_stamp.penup()
    image_stamp.setposition(0,125)
    printer_2.setposition(-275, 300)
    printer_2.color("White")
    if page == 1:
        printer_2.setposition(-100, 300)
        printer_2.write("Claim", font=Title_font)
        printer_2.setposition(-500, -400)
        printer_2.write("The British did not bring much progress to South Africa. From severely limited representation for the Africans, to\ndscientific racism, and a military designed to protect British assets and gain land, the British colonized Africa solely\nfor profit.For starters, many colonies had little representation and were reserved for European men who owned land,\nwith Africans having unfair voting qualifications, thus leading to the suppression of their voices. Additionally,\nthe rights of the Africans were basically non-existent, as laws were made for their rights, but implementation was sparse\nand inconsistent, leaving many without. Scientific racism and enlightenment theory also contributed to the\nportrayal of Africans as uncivilized and inferior, with their land being stolen by the British military for their economic\ngains, leaving only small cultural reserves that were inadequate by far.\n                                       \nNow, some might mention how The Children’s Friend Society sent over 2,000 children to gain education and real-life \nexperience with apprenticeships, but they would be wrong. An investigation into the conditions of their education and\nwork revealed the “humanitarian” efforts to be a facade, with many children receiving little to no education, and those\nwho did learned only what they needed to work in jobs such as woodworking, gardening, and bookbinding. Others \nmight also mention how the British tried to abolish slavery and child labor in the colonies, but that was merely a front\nto seize and annex the relatively peaceful Boer Republics of Transval and the Orange Free State, to be used to\nmine gold and diamonds for European profit, and to create plantations for the export of raw goods. These plantations,\nestablished for the growing of sugar, coffee, cacao, and other tropical products, ravaged the local forests for\nland and resources. They also practiced monoculture, which is detrimental to soil sustainability,with the lack\nof biodiversity making plants vulnerable to disease and insects.", font=paragraph_font)
        image_stamp.setposition(-25, 175)
        image_stamp.shape(claim)
        printer_2.setposition(200,150)
        printer_2.write("The war against Transval.", font=paragraph_font)
    elif page ==2:
        printer_2.write("Background Info", font=Title_font)
        printer_2.setposition(-500, -250)
        printer_2.write("In the 17th century, the Cape Town region of South Africa was settled by the Dutch East India Company, called Boers.\nThey were independent slave-owners and resented the British government when it abolished slavery. So, they decided\nto move out of British control, creating the Orange Free State and the Transvaal Republic, slaughtering the local Zulu\npopulation nearby.\n                                                                                             \nThe British gained control over the Cape Colony in the early 1800s, following the bankruptcy of the Dutch East India\nCompany and several significant battles, such as the Battle of Blaauwberg in 1806.  Regardless, Britain’s control\nover the Cape Colony in South Africa was first recognized as part of the Congress of Vienna in 1815.", font=paragraph_font)
        image_stamp.setposition(-30, 125)
        image_stamp.shape(orange_state_flag)
        printer_2.setposition(200,120)
        printer_2.write("The Orange Free State Flag", font=paragraph_font)
    elif page ==3:
        printer_2.write("Economic Progress", font=Title_font)
        printer_2.setposition(-500, -200)
        printer_2.write("The British landowners and employers benefited greatly from the use of cheap, African labor. With the Master and Servant\nAct of 1823, the employee was at a severe disadvantage, as they could be fired, put in jail, or be docked pay\nfor any breach of contract. The employer, who could be charged, would be requested to attend a hearing, but then the\nemployee, when charged, would be arrested first. The nature of legislation and its impact on the employment contract\nmeant that in many instances, employees could not negotiate a fair contract. This is made even worse when we look at how a\nservant is defined as “an employee whose function is to render service”(Swiegers, 81).", font=paragraph_font)
        image_stamp.shape(economy)
        printer_2.setposition(300,120)
        printer_2.write("African people being collected\nfor forced labor.", font=paragraph_font)
    elif page ==4:
        printer_2.write("Religious Progress", font=Title_font)
        printer_2.setposition(-500, -150)
        printer_2.write("Religious beliefs and missions were closely connected to commercial activities. The belief that the only way to promote\nChristianity was using trade in the colonies. In the 1800's, new systems were implemented in witch “religious\neducation were neglected,”(Swiegers, 213) but laws were soon made protecting freedom of religion and property. However,\nimplementation of these was sparse and inconsistent, with many Africans not receiving these rights.", font=paragraph_font)
        image_stamp.shape(religous)
        printer_2.setposition(250,125)
        printer_2.write("A African child in Christian Mission.", font=paragraph_font)
    elif page ==5:
        printer_2.setposition(-250, 300)
        printer_2.write("Social Progress", font=Title_font)
        printer_2.setposition(-500, -275)
        printer_2.write("The English men in the colonies were favored by the government. Scientific racism played major role in colonies at this time\nwith placing “indigenous groups on the lower levels of development”. Indigenous groups were portrayed as\nuncivilised and inferior. This lead to the civil and political rights of African and other non-white groups were basically\nnon-existent.", font=paragraph_font)
        image_stamp.shape(social)
        image_stamp.setposition(0,70)
        printer_2.setposition(200,100)
        printer_2.write("A chart use to decid who was \ntreated how through social racsim.", font=paragraph_font)
    elif page ==6:
        printer_2.setposition(-325, 300)
        printer_2.write("Intellectual Progress", font=Title_font)
        printer_2.setposition(-500, -200)
        printer_2.write("During this time enlightment ideals were staring to spread becomeing very prominent in the colonies of Britian, especially\nsientific ones. Some of them were about sientific racism and others ideas of how people “could develop through\nexposure to education and science”(Swieger,17). Even though many ideas were accepted, this didn't stop arguments about science vs.\nreligen. Although many people had started to belive the scientific idea of phrenology that stated people\nwere not able to change because their actions could always be traced back to biological impluses. But religion stated people adapted to\nthe enviroment around them and were able to change.", font=paragraph_font)
        image_stamp.shape(burden) 
        image_stamp.setposition(-25,125)
        printer_2.setposition(185,125)
        printer_2.write("The political cartoon a white mans burden.", font=paragraph_font)
    elif page ==7:
        printer_2.setposition(-325, 300)
        printer_2.write("Government Progress", font=Title_font)
        printer_2.setposition(-500, -200)
        printer_2.write("Colonies that had a majority of European colonists had a more a government closser to a monarchy, where the executive branch\nmakes all the decisions. Colonies that had less European colonists had representative government, and giving\nthem an actual say. The Cape Colony elected its first parliament in 1854, but remained under the control of the British.\nAlthough shortly after 1881 the “British government granted self-governance to the Cape and Natal colonies”\n(Dalvoy,Paragraph 6).", font=paragraph_font)
        image_stamp.shape(government)
        printer_2.setposition(250,150)
        printer_2.write("A meeting of the exectutive \nbranch in the cape colony.", font=paragraph_font)
    elif page ==8:
        printer_2.setposition(-325, 300)
        printer_2.write("Environment Progress", font=Title_font)
        printer_2.setposition(-500, -200)
        printer_2.write("The plantations, which were established for sugar, coffee, cacao, and other tropical products, ravaged the local forests\nfor land and resources. They also practiced monoculture, which is detrimental to soil sustainability, “reduces\nbiodiversity” (Kaur,1),and with a lack of biodiversity making it vulnerable to disease and bugs.", font=paragraph_font)
        image_stamp.setposition(0,100)
        image_stamp.shape(envrioment)
        printer_2.setposition(250,100)
        printer_2.write("People working at a plantation \npreforming monoculture.", font=paragraph_font)
    elif page ==9:
        printer_2.setposition(-250, 300)
        printer_2.write("Military Progress", font=Title_font)
        printer_2.setposition(-500, -150)
        printer_2.write("The military was used to suppress and drive out the natives for more land use. Like the “military expansion of the Zulu\nKingdom, which was located roughly in the eastern sections of South Africa”(Beck,Paragraph 11). Along with when the\nXhosa attacked the Cape Colony, the military fought them and took their land. They also annexed the Orange Free State\nand the Transval area, which were independent and relatively peaceful. In the end, the military was really only\nto protect the British investments in the area.", font=paragraph_font)
        image_stamp.shape(transval_flag)
        printer_2.setposition(200,120)
        printer_2.write("The Transval Flag", font=paragraph_font)
    elif page ==10:
        printer_2.setposition(-275, 300)
        printer_2.write("Education Progress", font=Title_font)
        printer_2.setposition(-500, -200)
        printer_2.write("Education was limited, with most children being put to work without education, or only educated to do their jobs, such\nas gardening, woodwork, and bookbinding. Their culture was portrayed as inferior and not respected or upheld. Their\nwas a investigation of the treatment of the kids in the Childrens Friend Society and it was found that “employers were in many instances\n were not concerned with training apprenticed children”(Swieger,159)", font=paragraph_font)
        image_stamp.shape(education)
        image_stamp.setposition(0,100)
        printer_2.setposition(200,100)
        printer_2.write("Children in The Childrens Friend Society\nwho are being sent to work, without\ngetting a education.", font=paragraph_font)
    elif page ==11:
        printer_2.setposition(-250, 300)
        printer_2.write("Political Progress", font=Title_font)
        printer_2.setposition(-500, -250)
        printer_2.write("Colonies with fewer Europeans in them had representative government and more of a say. In the period before the Cape\nreceived representative government in 1853, the governor had full control over the enactment of legislation. Although\nrepresentation was granted, only men who owned land could vote. Progress in getting representation for other people was\nslow but as more times passed laws like Ordinance No. 50 were passed, “Ordinance No. 50 awarded civil and legal\nrights to the Khoikhoi and other previously disadvantaged groups by ensuring their freedom of movement and allowing them\nto own land”(Swiegers,33).", font=paragraph_font)
        image_stamp.shape(political)
        printer_2.setposition(300,150)
        printer_2.write("Union Of South Africa.", font=paragraph_font)
    elif page ==12:
        printer_2.setposition(-125, 300)
        printer_2.write("Sources", font=Title_font)
        printer_2.setposition(-500, -400)
        printer_2.write("1. Beinart, William. “African History and Environmental History.” JSTOR, \nwww.jstor.org/stable/723810. Accessed 20 Feb. 2026.\n\n2. “Doctrines of Racial Segregation in Britain: 1900–1944.” New Community, 1984, \nhttps://doi.org/10.1080/1369183X.1984.9975871. \n\n3. “European Imperialism in South Africa.” History Crunch, 2022, \nwww.historycrunch.com/european-imperialism-in-south-africa.html. Accessed 20 Feb. 2026.\n\n4. Heritage History. “Heritage History – Products.” Heritage History, 2025, \nwww.heritage-history.com/index.php?c=resources&s=study-qdiv&h=british_empire&f=africa. Accessed 20 Feb. 2026.\n\n5. Keith, G. K. Utopia of Usurers and Other Essays. Project Gutenberg, \nwww.gutenberg.org/cache/epub/2134/pg2134-images.html. Accessed 20 Feb. 2026.\n\n6. “Monoculture of Crops: A Challenge in Attaining Food Security.” Advances in Food Security and Sustainability, 2024, pp. 197–213, \nhttps://doi.org/10.1016/bs.af2s.2024.07.008. \n\n7.“(Re)creating Spaces for uMunthu: Postcolonial Theory and Environmental Education in Southern Africa.”\nEnvironmental Education Research, 2013, https://doi.org/10.1080/13504622.2013.860428. \n\n8. Rich, Paul. “British Imperial Policy, Trusteeship and the Appeasement of White South African Power, \n1929–1939.” Collected Seminar Papers, vol. 40, Institute of Commonwealth Studies, 1990, pp. 12–23, \nsas-space.sas.ac.uk/4204/1/Paul_Rich_-_British_imperial_policy,_trusteeship_and_the_appeasement_of_white_South_African_power,_1929-1939.pdf.\n\n9. Swiegers, Gerhard M. Britain and the Labour Question in South Africa: The Interaction of State, Capital, Labour and Colonial Power, \n1867–1910. Doctoral dissertation, University of the Free State, 2014, \nscholar.ufs.ac.za/server/api/core/bitstreams/929f8aa8-f0e9-4679-84ce-394c476de828/content.\n\n10. Team, D. E. “British Imperialism in South Africa (1800–1907) | UPSC Mains History-Paper-II 2016.” Dalvoy, 29 Dec. 2025,\nwww.dalvoy.com/en/upsc/mains/previous-years/2016/history-paper-ii/british-imperialism-south-africa. Accessed 20 Feb. 2026.\n\n11. “The Struggle for the Land.” Google Books, \nbooks.google.com/books?hl=en&lr=&id=OqwF27HZms8C&oi=fnd&pg=PA146. Accessed 20 Feb. 2026.\n\n12. Van Helten, J.-J. British Capital, the British State and Economic Investment in South Africa, \n1886–1914. Collected Seminar Papers, no. 24, Institute of Commonwealth Studies, 1979, \nsas-space.sas.ac.uk/4066/1/J_J_van_Helten_-_British_capital,_the_British_state_and_economic_investment_in_South_African_1886-1914.pdf.", font=source_font)   
        image_stamp.hideturtle()
    wn.update()
    button_home.onclick(home_page)
    
home_page(1,1)
    
wn.mainloop()