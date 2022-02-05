    if message.content.startswith("(봇이름)배워"):
        await message.channel.send(embed=discord.Embed(title="단어추가",description="추가하실 단어를 입력해주세요.",color=0x5c6cdf))
        def check(words):
            return (words.author.id == message.author.id)
        words = await client.wait_for("message", timeout=60, check=check)
        words = words.content
        await message.channel.send(embed=discord.Embed(title="뜻추가",description=words + "의 뜻을 입력해주세요.",color=0x5c6cdf))
        def check(mean):
            return (mean.author.id == message.author.id)
        mean = await client.wait_for("message",timeout=60,check=check)
        mean = mean.content
        fuckyou = await message.channel.send(embed=discord.Embed(title="`" + words + "`를 추가하시겠습니까?\n 뜻 : `" + mean + "`",description="예/아니요로 답해주세요.",color=0x5c6cdf))
        def check(answer):
            return (answer.author.id == message.author.id)
        answer = await client.wait_for("message", timeout=60, check=check)
        answer = answer.content
        if answer == "아니요":
            await fuckyou.edit(embed=discord.Embed(title="취소",description="성공적으로 단어 추가를 취소하였습니다.",color=0x5c6cdf))
            return
        if answer == "예":
            con = sqlite3.connect("../DB/" + "words.db")
            cur = con.cursor()
            cur.execute("INSERT INTO words VALUES(?,?,?);",(str(message.author), words, mean))
            con.commit()
            con.close()
            await message.channel.send("추가완료")
        else:
            await message.channel.send("추가실패")

    

    if message.content.startswith("(봇이름) "):
        find = message.content.split(" ")[1]
        con = sqlite3.connect("../DB/" + "words.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM words WHERE word == ?;", (find,))
        words_info = cur.fetchone()
        con.close()
        await message.channel.send(f"단어 : {words_info[1]}\n뜻 : {words_info[2]}\n```이 단어는 {words_info[0]}님께서 알려주셨어요!```")
        


            
    if message.content.startswith("!단어삭제 "):
        if message.author.id == int(admin_id):
            word = message.content.split(" ")[1:]
            con = sqlite3.connect("../DB/" + "words.db")
            cur = con.cursor()
            cur.execute("DELETE FROM words WHERE word == ?;",(word,))
            con.commit()
            con.close()
            await message.channel.send(embed=discord.Embed(title="삭제성공",description="삭제된 단어 : " + str(word),color=0x5c6cdf))
