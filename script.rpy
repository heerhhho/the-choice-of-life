# Определение персонажей игры.
define a = Character('Влад Покровский', color="#6A92E3")
define b = Character('Паша Зорин', color="#ab5805")
define c = Character('Света Петрова', color="#e675c0")
define e = Character('Мать Влада', color="#ffffff")
define f = Character('Отец Влада', color="#ffffff")
define g = Character('Мать Паши', color="#ffffff")
define h = Character('Отец Паши', color="#ffffff")
define i = Character('???', color="#ffffff")

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре/
# play music "audio/название файла (ogg)" - включить музыку

image p stand:
    "images/п стоит.png"
    zoom 0.5

image p stand_eye:
    "images/п стоит глаза.png"
    zoom 0.5

image p stand2:
    "images/п стоит рот.png"
    zoom 0.5

image p stand_eye2:
    "images/п стоит рот глаза.png"
    zoom 0.5

image p stand_hand:
    "images/п стоит руки.png"
    zoom 0.5

image p stand_hand2:
    "images/п стоит руки глаза.png"
    zoom 0.5

image p idk:
    "images/п хз.png"
    zoom 0.5

image p idk2:
    "images/п хз рот.png"
    zoom 0.5

image p cry:
    "images/п плакса.png"
    zoom 0.5

image p cry2:
    "images/п плакса слез.png"
    zoom 0.5

image p offended:
    "images/п обижен.png"
    zoom 0.5

image p offended2:
    "images/п обижен рот.png"
    zoom 0.5

image p libido:
    "images/п либидо.png"
    zoom 0.5

image p libido2:
    "images/п либидо рот.png"
    zoom 0.5

image v stand:
    "images/в крут.png"
    zoom 0.5

image v stand2:
    "images/в крут рот.png"
    zoom 0.5

image v idk:
    "images/в хз.png"
    zoom 0.5

image v idk2:
    "images/в хз рот.png"
    zoom 0.5

image v scare:
    "images/в испуг.png"
    zoom 0.5

image v shame:
    "images/в стыд.png"
    zoom 0.5
   
image v shame2:
    "images/в стыд рот.png"
    zoom 0.5

image v think:
    "images/в думает.png"
    zoom 0.5

image v think2:
   "images/в думает рот.png"
   zoom 0.5
    
transform scared:
    yoffset 0
    ease 0.05 yoffset -18
    ease 0.08 yoffset 5
    ease 0.12 yoffset 0

transform scared2:
    yoffset 0
    ease 0.09 yoffset 3
    ease 0.09 yoffset 0
    repeat

transform walk:
    xalign 0.5
    yalign 1.0
    yoffset 0
    ease 0.7 yoffset -10
    ease 0.7 yoffset 0
    repeat

transform walk2:
    xalign 0.5
    yalign 1.0
    yoffset 0
    ease 0.3 yoffset -10
    ease 0.3 yoffset 0
    repeat

transform emotion:
    yoffset 0
    linear 0.03 xoffset -3
    linear 0.03 xoffset 3
    linear 0.03 xoffset -2
    linear 0.03 xoffset 0

label before_main_menu:
    play music "audio/Paulie_Leparik_Middy_Tiddy[1].ogg" fadein 2.0
    return

label start:

"202? год, 16 декабря."

scene v cry with dissolve

"В комнате было убийственно тихо."

"Влад лежал на кровати, смотря в никуда. Он даже не успел переодеться после возвращения домой, лишь скинув с себя верхнюю одежду."

"Всё что ему сейчас хотелось - чтобы этот невыносимый день наконец закончился."

"Он попытался успокоиться, но мысли снова и снова возвращались к произошедшему."

"От этого становилось только {color=#4F0101}хуже.{/color}"

play sound "audio/vibro.ogg"

"Телефон коротко завибрировал рядом с ним."

"Новое сообщение."

scene v cry2 with dissolve

show expression im.Scale("images/тилефон.png", 800, 1030) as phone zorder 1 at right

show expression im.Scale("images/ты уже дома.png", 800, 1030) as msg1 zorder 2 at right

show expression im.Scale("images/трещины.png", 800, 1030) as cracks zorder 30 at right

"Это было то самое рыжее недоразумение, которое почти всегда писало Владу."

show expression im.Scale("images/да.png", 800, 1030) as msg2 zorder 3 at right 
pause

show expression im.Scale("images/тебя прям сильно тошнило.png", 800, 1030) as msg3 zorder 4 at right 
pause

show expression im.Scale("images/ты какой-то плохой был.png", 800, 1030) as msg4 zorder 5 at right 
pause

show expression im.Scale("images/не знаю.png", 800, 1030) as msg5 zorder 6 at right 
pause

show expression im.Scale("images/просто там находиться было мерзко.png", 800, 1030) as msg6 zorder 7 at right 
pause

hide msg1
hide msg2
hide msg3
hide msg4
hide msg5
hide msg6

show expression im.Scale("images/из-за чего.png", 800, 1030) as msg7 zorder 8 at right 
pause

show expression im.Scale("images/не хочу сейчас об этом.png", 800, 1030) as msg8 zorder 9 at right 
pause

show expression im.Scale("images/ладно.png", 800, 1030) as msg9 zorder 10 at right 
pause

show expression im.Scale("images/я не буду давить.png", 800, 1030) as msg10 zorder 11 at right 
pause

show expression im.Scale("images/но ты можешь рассказать если хочешь.png", 800, 1030) as msg11 zorder 12 at right 
pause

menu:
    "мне просто плохо в последнее время.":
        hide msg7
        hide msg8
        hide msg9
        hide msg10
        hide msg11
        show expression im.Scale("images/мне просто плохо в последнее время.png", 800, 1030) as msg12 zorder 13 at right 
        pause
        show expression im.Scale("images/не только сегодня.png", 800, 1030) as msg13 zorder 14 at right 
        pause
        show expression im.Scale("images/я заметил. Давно так.png", 800, 1030) as msg14 zorder 15 at right 
        pause
    "Забей, ничего особенного.":
        hide msg7
        hide msg8
        hide msg9
        hide msg10
        hide msg11
        show expression im.Scale("images/да забей.png", 800, 1030) as msg15 zorder 16 at right  
        pause
        show expression im.Scale("images/я же не просто так спрашиваю.png", 800, 1030) as msg17 zorder 18 at right 
        pause
    "Я сам не понимаю, что со мной.":
        hide msg7
        hide msg8
        hide msg9
        hide msg10
        hide msg11
        show expression im.Scale("images/я сам не понимаю что со мной.png", 800, 1030) as msg18 zorder 19 at right 
        pause
        show expression im.Scale("images/я даже обьяснить нормально не могу.png", 800, 1030) as msg19 zorder 20 at right 
        pause
        show expression im.Scale("images/тогда и не обьясняй нормально.png", 800, 1030) as msg20 zorder 21 at right 
        pause
        show expression im.Scale("images/можешь просто написать, как есть.png", 800, 1030) as msg21 zorder 22 at right 
        pause

hide msg12
hide msg13
hide msg14
hide msg15
hide msg17
hide msg18
hide msg19
hide msg20
hide msg21

show expression im.Scale("images/ладно, может прогуляемся.png", 800, 1030) as msg22 zorder 23 at right
pause
show expression im.Scale("images/я не против.png", 800, 1030) as msg23 zorder 24 at right
pause

scene v cry with dissolve

"Влад отложил телефон и ещё несколько секунд смотрел в стену."

"Идти куда-то совершенно не хотелось, но оставаться в комнате тоже."

"Он медленно поднялся с кровати, нашёл на спинке студа чистую кофту и переоделся."

scene black

"Перед выходом пришлось несколько раз проверить карманы: телефон, ключи, наушники. Всё на месте."

"Паша уже успел отправить ещё одно сообщение."

show expression im.Scale("images/тилефон.png", 800, 1030) as phone zorder 1 at right

show expression im.Scale("images/через сколько будешь.png", 800, 1030) as msg1 zorder 2 at right
pause

a "какой он нетерпеливый..."

show expression im.Scale("images/трещины.png", 800, 1030) as cracks zorder 30 at right

show expression im.Scale("images/минут через десять.png", 800, 1030) as msg2 zorder 3 at right
pause

show expression im.Scale("images/ебануться.png", 800, 1030) as msg3 zorder 4 at right
pause

show expression im.Scale("images/я уже соскучился.png", 800, 1030) as msg4 zorder 5 at right
pause

hide phone
hide cracks
hide msg1
hide msg2
hide msg3
hide msg4

show v shame at walk

"На улице было темно и довольно тихо. Небо затянули тяжёлые облака, а редкие фонари, которым самим было стыдно, освещали покрытые снегом дороги."

"Воздух неприятно холодил лицо, стоило только выйти из подъезда."

"Где-то вдали проезжали редкие машины, оставляя после себя шуршание шин по мокрому асфальту."

"Изо рта при каждом вдохе вырывался небольшой клубок пара."

show v shame at walk2

"Влад машинально прячет руки в глубь карманов и ускоряет шаг, понимая, что таким образом он всё равно будет ждать этого вечно опаздывающего одноклеточного."

pause 2.0

show v shame at emotion

"Дойдя до огромного дерева, где ещё с младенческих лет остались их инициалы, Влад присел на мокрый от влажности погоды пень и стал ожидать." 

"Ожидать пришлось долго: пока этот лимитированный ебалай соберётся, пройдёт несколько лет."

"И всегда вместо прогулки ты получишь лишь отказ только потому, что ёбырь опять решил провести время с женскими особями,"

"Вместо того, чтобы погулять с другом, которого ты знаешь почти с пелёнок."

show v scare at scared

a "Другом..."

a "А он вообще считает меня своим другом?"

menu:
    "Думаю, да.":
        show v think2
        a "Сколько мы дружим, он ни разу не жаловался..."
    "Думаю, нет.":
        show v think2
        a "Мне кажется, что он просто боится это сказать."

show v shame2 

"Ветер завыл сильнее, будто стараясь вынести все грехи из этого бледного и бездыханного тела. Влад зарылся сильнее в куртку, стараясь не замёрзнуть."

a "Да где этот микроб..."

"Из сугроба вдруг доносится:"

show v scare at scared

i "Сам ты микроб!"

"Ветер, всё ещё кружащий вокруг Влада, начала сметать белюшок с сугроба, раскрывая бедную картину."

i "Эй, чего смотришь? Помоги выбраться!"

show v stand2 at emotion

a "Блять, это ты..."

show v stand at emotion

"Влад наблюдал, как этот рыжий пончик с покрасневшим еблом от холода, валяющий в снегу, пытался выбраться."

"И этого рыжего пончика зовут..."

show v scare at scared

a "Паша! Отпусти!"

###

show v stand at left

show p libido2 at right

b "Крутое появление, согласись."

show p libido at emotion

## здесь должен быть спрайт крутго влада

show v stand2 at emotion

a "Да. Особенно понравилась часть, где я чуть не умер."

show v stand at emotion

show p libido2 at emotion

b "Значит, я произвёл впечатление!"

show v stand2 at emotion

show p libido at emotion

a "К сожалению."

show v stand at emotion

show p stand_hand2 at emotion

b "Почему 'к сожалению'?"

show p stand_hand at emotion

show v stand2 at emotion

a "Потому что ты еблан."

show v stand at emotion

show p stand2 at emotion 

b "Это комплимент?"

show v stand2 at emotion

show p stand at emotion

a "Это диагноз."

show v stand at emotion

show p offended2 at emotion

b "Ладно, ты выиграл."

show v stand2 at emotion

show p offended at emotion

a "Но долбаёбом ты остаёшься не только в рамках нашей 'игры'."

"Паша на секунду замолчал, будто всерьёз обдумывая последние слова Влада. Затем он театрально приложил руку к груди."

b "Жестоко. А я ведь старался."

### спрайт крутого влада

a "Вот именно. В следующий раз не старайся."

b "Да ты просто завидуешь моему таланту."

a "Какому именно? Лежать в снегу и изображать сугроб?"

b "Между прочим, это была сложная тактическая операция."

a "Ты не мог встать."

b "Это часть операции!"

"Влад тихо усмехнулся и отвёл взгляд. Паша  заметил это, но комментировать не стал - вместо этого принялся отряхивать снег с куртки. Несколько комков упали прямо на ботинки Влада."

a "Эй."

b "Что ты уже экаешь?"

a "Ты мне снегом всё засыпал."

b "Он сам упал."

a "Конечно. У него тоже тактическая операция."

"Паша довольно хмыкнул и наконец приводить себя в порядок. Потом посмотрел на Влада, который всё ещё сидел на пне."

b "Ну что, пойдём?"

a "И куда же?"

b "Гулять. Мы же не для того сюда пришл, чтобы ты полчаса сидл на пеньке и мёрз."

a "Вообще-то я именно этим и занимался до твоего появления."

b "Вот и займёмся чем-нибудь более интересным."

"Влад нехотя поднялся, поправил куртку и сунул руки в карманы."

a "Надеюсь, в следующий раз ты хотя бы не будешь притворяться снеговиком."

b "Ничего не обещаю."