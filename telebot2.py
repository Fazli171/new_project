from telebot import TeleBot , types

bot = TeleBot(token='7994405449:AAE4E91FgtzCJacRO94WSdcpQkDcPlBp-04')
try:
    tugmalar = types.ReplyKeyboardMarkup(row_width= 2,resize_keyboard=True)
    binary = types.KeyboardButton(text='decimal(10) -> binary(2)')
    matnga = types.KeyboardButton(text='biray(2) -> decimal(10)')
    octal = types.KeyboardButton(text='decimal(10) -> octal(8)')
    octal_matn = types.KeyboardButton(text='octal(8) -> decimal(10)')
    hex = types.KeyboardButton(text='decimal(10) -> hex(16)')
    hex_matn = types.KeyboardButton(text='hex(16) -> decimal(10)')
    help = types.KeyboardButton(text='help')
    new_line = '\n' 


    tugmalar.add(binary,matnga,octal,octal_matn,hex,hex_matn,help)

    @bot.message_handler(commands=["start"])
    def star(xabar:types.Message):
        bot.send_message(xabar.from_user.id, "quyidali amallarni tanlang",
                        reply_markup=tugmalar)
    @bot.message_handler(func=lambda x : True)
    def tekshir(xabar: types.Message):
        match xabar.text:
            case "decimal(10) -> binary(2)":
                bot.send_message(xabar.from_user.id,'decimal(10) -> binary(2) malumotini kriting')
                bot.register_next_step_handler(xabar,natija2)
            case 'biray(2) -> decimal(10)':
                bot.send_message(xabar.from_user.id , 'biray(2) -> decimal(10) malumotini kriting')
                bot.register_next_step_handler(xabar,natija)
            case 'decimal(10) -> octal(8)':
                bot.send_message(xabar.from_user.id , 'decimal(10) -> octal(8) malumotini kriting')
                bot.register_next_step_handler(xabar,natija8)
            case 'decimal(10) -> hex(16)':
                bot.send_message(xabar.from_user.id , "decimal(10) -> hex(16) makumotini kriting")
                bot.register_next_step_handler(xabar,natija16)
            case 'octal(8) -> decimal(10)':
                bot.send_message(xabar.from_user.id , "octal(8) -> decimal(10) malumotini kriting")
                bot.register_next_step_handler(xabar,natija81)          
            case 'hex(16) -> decimal(10)':
                bot.send_message(xabar.from_user.id ,'hex(16) -> decimal(10) malumotini kriting')
                bot.register_next_step_handler(xabar,natija161)  
            case 'help':
                help_text = (
                "Sizning kodingizda xato MarkdownV2 formatida yuborilayotgan xabar bilan bog'liq.\n"
                "MarkdownV2 formatida ba'zi maxsus belgilar (masalan, `-`, `_`, `*`, `~`, va boshqalar) "
                "Telegram tomonidan qoidaga muvofiq qochirilmog'i lozim, ya'ni oldiga `\\` qo'yilishi kerak.\n\n"
                "Masalan, agar matnda `-` belgisi bo'lsa, uni `\\-` deb yozish kerak."
                "qaysidir sanoq sistemasidan sonlar qiymadini decimial qaiymat chiqishida xato bo'lishi mumkun"
                "\nbo'g'lanish uchun @MAT2101S"
                )
                bot.send_message(xabar.from_user.id, help_text)
            

    def natija2(text:types.Message):
        try:
            chiqarish = []
            if text.text.isdigit(): 
                number = int(text.text)  
                chiqarish.append(format(number,'b')) 
                bot.send_message(text.from_user.id,f'binary qiymat✅  \n{chiqarish[0]}')
            else:
                lis = [format(ord(i), 'b') for i in text.text]
                binary_to_char = [i for i in text.text]
                nat = dict(zip(lis, binary_to_char))
                for k , v in nat.items():
                    i = f' {k}  🔄  {v}  '
                    chiqarish.append(i)
                bot.send_message(text.from_user.id, f"binary qiymat ✅ \n{new_line.join(chiqarish)} \n```\n{new_line.join(lis)}```\n", parse_mode='MarkdownV2')

        except ValueError:
            bot.send_message(text.from_user.id,"bot ayrim belgilarni qabul qilmaydi yoki nto'g'ro malimot\n ❌")
    def natija8(text:types.Message):
        try:
            chiqarish = []
            if text.text.isdigit():
                number = int(text.text)  
                chiqarish.append(format(number,'o')) 
                bot.send_message(text.from_user.id,f'octal qiymat \n✅  \n{chiqarish[0]}')            
            else:
                lis = [format(ord(i), 'o') for i in text.text]
                binary_to_char = [i for i in text.text]
                nat = dict(zip(lis, binary_to_char))
                chiqarish = []
                for k , v in nat.items():
                    i = f' {k}  🔄  {v} '
                    chiqarish.append(i)
                bot.send_message(text.from_user.id, f"octal qiymat ✅ \n{new_line.join(chiqarish)} \n```\n{new_line.join(lis)}```\n", parse_mode='MarkdownV2')

        except ValueError:
            bot.send_message(text.from_user.id,"bot ayrim belgilarni qabul qilmaydi yoki nto'g'ro malimot\n ❌")
    def natija161(xabar:types.Message):
        try:
            natija = []
            lis = xabar.text.split()
            for i in lis:
                nat = (int(i , 16))
                natija.append(chr(nat))
            bot.send_message(xabar.from_user.id, f"natija ✅ \n{''.join(natija)}")


        except ValueError:
            bot.send_message(xabar.from_user.id , "bot ayrim belgilarni qabul qilmaydi yoki nto'g'ro malimot\n ❌")   
    def natija81(xabar:types.Message):
        try:
            natija = []
            lis = xabar.text.split()
            for i in lis:
                nat = (int(i , 8))
                natija.append(chr(nat))
            bot.send_message(xabar.from_user.id, f"natija ✅  \n{''.join(natija)}")
        except ValueError:
            bot.send_message(xabar.from_user.id , "bot ayrim belgilarni qabul qilmaydi yoki nto'g'ro malimot\n ❌")
    def natija(text:types.Message):
        try:
            natija = ''
            lis = text.text.split()
            for a in lis:
                raqamlar = [int(i) for i in str(a)]
                summa = 0
                m = 0
                for i in range(len(raqamlar)-1 , -1 , -1):
                    summa += (2 ** i) * raqamlar[m]
                    m += 1
                natija += (chr(summa))
            bot.send_message(text.from_user.id, f'natija\n✅ \n{natija}' )
        except ValueError:
            bot.send_message(text.from_user.id , f"bot ayrim belgilarni qabul qilmaydi yoki nto'g'ro malimot\n ❌")
    def natija16(text:types.Message):
        try:
            chiqarish = []
            if text.text.isdigit():
                number = int(text.text)  
                chiqarish.append(format(number,'x')) 
                bot.send_message(text.from_user.id,f'hex qiymat \n✅  \n{chiqarish[0]}') 
            else:
                lis = [format(ord(i), 'x') for i in text.text]
                binary_to_char = [i for i in text.text]
                nat = dict(zip(lis, binary_to_char))
                for k , v in nat.items():
                    i = f' {k}  🔄  {v} '
                    chiqarish.append(i)
                bot.send_message(text.from_user.id, f"hex qiymat ✅ \n{new_line.join(chiqarish)} \n```\n{new_line.join(lis)}```\n", parse_mode='MarkdownV2')

        except ValueError:
            bot.send_message(text.from_user.id,"bot ayrim belgilarni qabul qilmaydi yoki nto'g'ro malimot\n❌")
            

    bot.polling(non_stop=True)
except Exception as e:
    print(f"Xatolik yuz berdi: {e}")