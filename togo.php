 <?php
$API_KEY = '6499198312:AAG1VAJHQ9pf0XD7UHA2Em5zXhisPxkgwe8'; // توكن
echo "https://api.telegram.org/bot$API_KEY/setwebhook?url=".$_SERVER['SERVER_NAME']."".$_SERVER['SCRIPT_NAME']; 

define('API_KEY',$API_KEY);
function bot($method,$datas=[]){
    $url = "https://api.telegram.org/bot".API_KEY."/".$method;
    $ch = curl_init();
    curl_setopt($ch,CURLOPT_URL,$url);
    curl_setopt($ch,CURLOPT_RETURNTRANSFER,true);
    curl_setopt($ch,CURLOPT_POSTFIELDS,$datas);
    $res = curl_exec($ch);
    if(curl_error($ch)){
        var_dump(curl_error($ch));
    }else{
        return json_decode($res);
    }
}
$admin = 5099564264; /*ايدي المطور*/
$update = json_decode(file_get_contents('php://input'));
$message = $update->message;
$from_id = $message->from->id;
$chat_id = $message->chat->id;
$text = $message->text;
$data = $update->callback_query->data;
$message_id = $update->callback_query->message->message_id;
$chat_id2 = $update->callback_query->message->chat->id;
$name = $update->message->from->first_name;
$username = $update->message->from->username;
if ($text == '/start' and $chat_id == 709960573 ) {
    if (!file_exists("make.txt")) {
        bot('sendmessage',[
            'chat_id'=>$chat_id,
            'text'=>"- اهلا بك يا 👋🏻؛ [$name](tg://user?id=$chat_id) ،
﹎﹎﹎﹎﹎﹎﹎﹎﹎﹎﹎﹎

- في بوت صنع بوتات الكتابة الخاص بك ، 📬'
- قم بصنع البوت الذي تريده الان ، 🌈'
- مع ميزة تغيير الحقوق من البوت ، 📌'
- ملاحظة ؛ لا يمكن لغيرك ان يصنع بوت ، 🇮🇶'
- هذا البوت خاص بالمطور فقط ، ⚙'
﹎﹎﹎﹎﹎﹎﹎﹎﹎﹎﹎﹎",
            'reply_markup'=>json_encode([
                'inline_keyboard'=>[
                    [['text'=>'• صنع بوت ، ❇️ •','callback_data'=>"make"],['text'=>'حذف بوت ','callback_data'=>'del']],
                   [['text'=>"- By ؛", "callback_data"=>"zhaemr"],['text'=>"@$username .", "callback_data"=>"zhaemr"]], 
                ]
            ])
        ]);
    } else {
        bot('sendmessage',[
            'chat_id'=>$chat_id,
            'text'=>"• اليك قائمةه تغيير حقوق البوت ، 🔰
• قم بتغيير ماتريد عند الانتهاء اضغط على زر صنع البوت ، 📢
﹎﹎﹎﹎﹎﹎﹎﹎﹎﹎﹎﹎",
            'reply_markup'=>json_encode([
                'inline_keyboard'=>[
                    [['text'=>'• تعديل ايدي المطور ، 🔗','callback_data'=>"setid"]],
                    [['text'=>'• تعديل معرف القناة ، 🌈','callback_data'=>"setch"]],
                    [['text'=>'• تعديل زر لشراء البوت ، ⚠️','callback_data'=>"setbuy"]],
                    [['text'=>"• صنع البوت ، 📌",'callback_data'=>'se']]
                ]
            ])
        ]);
    }
}
if($data == 'del'){
    bot('editMessageText',[
       'chat_id'=>$chat_id2,
       'message_id'=>$message_id,
       'text'=>'ارسل التوكن'
    ]);
    file_put_contents('mode.txt','del');
}
if ($data == 'make') {
    bot('sendmessage',[
            'chat_id'=>$chat_id2,
            'text'=>"• الان قم بارسال توكن البوت ، ☑️
• قم بجلب التوكن من @BotFather ، 📮
﹎﹎﹎﹎﹎﹎﹎﹎﹎﹎﹎﹎",
        ]);
        file_put_contents("mode.txt", "token");
}
if ($text != '/start' and file_get_contents("mode.txt") == 'token') {

    $get = json_decode(file_get_contents("https://api.telegram.org/bot$text/getme"))->result->username;
    if (isset($get)) {
        mkdir('bots');
        mkdir('bots/'.$text);
        bot('sendmessage',[
            'chat_id'=>$chat_id,
            'text'=>"• اليك قائمةه تغيير حقوق البوت ، 🔰
• قم بتغيير ماتريد عند الانتهاء اضغط على زر صنع البوت ، 📢
﹎﹎﹎﹎﹎﹎﹎﹎﹎﹎﹎﹎",
            'reply_markup'=>json_encode([
                'inline_keyboard'=>[
                    [['text'=>'• تعديل ايدي المطور ، 🔗','callback_data'=>"setid"]],
                    [['text'=>'• تعديل معرف القناة ، 🌈','callback_data'=>"setch"]],
                    [['text'=>'• تعديل زر لشراء البوت ، ⚠️','callback_data'=>"setbuy"]],
                    [['text'=>"• صنع البوت ، 📌",'callback_data'=>'se']]
                ]
            ])
        ]);
        file_put_contents("make.txt", $text);
        file_put_contents("mode.txt", "..");
    }

}

if ($data == 'se') {
bot('sendMessage',[
       'chat_id'=>$chat_id2,
       'text'=>"- اختر البوت الذي تود صنعه ; 🔱 !",
       'reply_markup'=>json_encode([
                'inline_keyboard'=>[	
                [['text'=>"• بوت زخرفةه ، ⚖ ؛",'callback_data'=>'mak'],['text'=>"• بوت الالعاب ، 🎮 ؛",'callback_data'=>'mak2']],
                    [['text'=>"• بوت الخيرة ، 📿 ؛",'callback_data'=>'mak3'],['text'=>"• قراءة الكف ، 🕊 ؛",'callback_data'=>'mak4']],
                    [['text'=>"• الحوت الازرق ، 🐬 ؛",'callback_data'=>'mak5'],['text'=>"• لعبة اكس او ، 🎌 ؛",'callback_data'=>'mak6']],
                    [['text'=>"• صنع بايو ، 〽️ ؛",'callback_data'=>'mak7'],['text'=>"• صنع متحركه ، 🎆 ؛",'callback_data'=>'mak8']],
                    [['text'=>"• ترتيب الكلام ، 🇮🇶 ؛",'callback_data'=>'mak9'],['text'=>"• لو خيروك ، 🌈 ؛",'callback_data'=>'mak10']],
                    [['text'=>"• العبارات الجدارية ، 🍄 ؛",'callback_data'=>'mak11'],['text'=>"• بوت الابراج ، 🐳 ؛",'callback_data'=>'mak12']],
                    [['text'=>"• حزورة بليرة ، 🚩 ؛",'callback_data'=>'mak13'],['text'=>"• كتابة ع صور ، 🎇 ؛",'callback_data'=>'mak14']],
                    [['text'=>"• بوت المحيبس ، ✊🏻 ؛",'callback_data'=>'mak15'],['text'=>"• زيادة الاعضاء ، 📬 ؛",'callback_data'=>'mak16']],
                    [['text'=>"• تحميل من ميوزكلي ، Ⓜ️ ؛",'callback_data'=>'mak17']],
                    [['text'=>"• تحميل من الانستا ، 📽 ؛",'callback_data'=>'mak18']],
                    [['text'=>"• تحميل من اليوتيوب ، 📕 ؛",'callback_data'=>'mak19']],
                    [['text'=>"• بوت الرصيد ، 💶 ؛",'callback_data'=>'mak20'],['text'=>"• حمايةه قنوات ، 🛡؛",'callback_data'=>'mak21']],
                    [['text'=>"• بوت التطبيقات ، 🛒 ؛",'callback_data'=>'mak22'],['text'=>"• بوت الفوتوشوب ، 📇 ؛",'callback_data'=>'mak23']],
                    [['text'=>"• بوت الارقام ، 🔮 ؛",'callback_data'=>'mak24'],['text'=>"• بوت اهمسلي ، 💬 ؛",'callback_data'=>'mak25']],
                    [['text'=>"• فيديو انستا ، 💢 ؛",'callback_data'=>'mak26'],['text'=>"• بوت المواصفات ، 🌟 ؛",'callback_data'=>'mak27']],
                    [['text'=>"• هل تعلم ، ❕؛",'callback_data'=>'mak28'],['text'=>"• بوت الخلفيات ، 📮 ؛",'callback_data'=>'mak29']],
                    [['text'=>"- Saad Mohammed ; 🔱 !!",'url'=>'t.me/sssbs']],
                        ]
            ])
        ]);
    }
    
if ($data == 'setid') {
    file_put_contents("mode.txt", "ids");
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>"دز الايدي"
    ]);
}
if($text and file_get_contents('mode.txt') == 'del'){
    if(is_dir('bots/'.$text)){
        $sc = scandir('bots/'.$text);
        foreach($sc as $k => $v){
            unlink('bots/'.$text.'/'.$v);
        }
        rmdir('bots/'.$text);
        bot('sendMessage',['chat_id'=>$chat_id,'text'=>'تم الحذف']);
    } else {
        bot('sendmessage',['chat_id'=>$chat_id,'text'=>'لم يتم صنع اي بوت بهذا التوكن']);
    }
    unlink('mode.txt');
}
elseif(preg_match('/[0-9]/',$text)  and file_get_contents("mode.txt") == 'ids') {
        file_put_contents("bots/".file_get_contents("make.txt").'/ids.txt', $text);

    bot('sendmessage',[
            'chat_id'=>$chat_id,
            'text'=>"• اليك قائمةه تغيير حقوق البوت ، 🔰
• قم بتغيير ماتريد عند الانتهاء اضغط على زر صنع البوت ، 📢
﹎﹎﹎﹎﹎﹎﹎﹎﹎﹎﹎﹎",
            'reply_markup'=>json_encode([
                'inline_keyboard'=>[
                    [['text'=>'• تعديل ايدي المطور ، 🔗','callback_data'=>"setid"]],
                    [['text'=>'• تعديل معرف القناة ، 🌈','callback_data'=>"setch"]],
                    [['text'=>'• تعديل زر لشراء البوت ، ⚠️','callback_data'=>"setbuy"]],
                    [['text'=>"• صنع البوت ، 📌",'callback_data'=>'se']]
                ]
            ])
        ]);
        file_put_contents("mode.txt", "..");
}

if ($data == 'setch') {
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>"دز القناه"
    ]);
    file_put_contents("mode.txt", "ch");
}
elseif($text and file_get_contents("mode.txt") == 'ch') {
        file_put_contents("bots/".file_get_contents("make.txt").'/ch.txt', $text);

    bot('sendmessage',[
            'chat_id'=>$chat_id,
            'text'=>"• اليك قائمةه تغيير حقوق البوت ، 🔰
• قم بتغيير ماتريد عند الانتهاء اضغط على زر صنع البوت ، 📢
﹎﹎﹎﹎﹎﹎﹎﹎﹎﹎﹎﹎",
            'reply_markup'=>json_encode([
                'inline_keyboard'=>[
                    [['text'=>'• تعديل ايدي المطور ، 🔗','callback_data'=>"setid"]],
                    [['text'=>'• تعديل معرف القناة ، 🌈','callback_data'=>"setch"]],
                    [['text'=>'• تعديل زر لشراء البوت ، ⚠️','callback_data'=>"setbuy"]],
                    [['text'=>"• صنع البوت ، 📌",'callback_data'=>'se']]
                ]
            ])
        ]);
        file_put_contents("mode.txt", "..");
}
if ($data == 'setbuy') {
    file_put_contents("mode.txt", "buy");
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>"دز المعرف"
    ]);
}
elseif($text  and file_get_contents("mode.txt") == 'buy') {
        file_put_contents("bots/".file_get_contents("make.txt").'/buy.txt', $text);

    bot('sendmessage',[
            'chat_id'=>$chat_id,
            'text'=>"• اليك قائمةه تغيير حقوق البوت ، 🔰
• قم بتغيير ماتريد عند الانتهاء اضغط على زر صنع البوت ، 📢
﹎﹎﹎﹎﹎﹎﹎﹎﹎﹎﹎﹎",
            'reply_markup'=>json_encode([
                'inline_keyboard'=>[
                    [['text'=>'• تعديل ايدي المطور ، 🔗','callback_data'=>"setid"]],
                    [['text'=>'• تعديل معرف القناة ، 🌈','callback_data'=>"setch"]],
                    [['text'=>'• تعديل زر لشراء البوت ، ⚠️','callback_data'=>"setbuy"]],
                    [['text'=>"• صنع البوت ، 📌",'callback_data'=>'se']]
                ]
            ])
        ]);
        file_put_contents("mode.txt", "..");
}

if ($data == 'mak') {
	$getMe = bot('getMe')->result;
    $file = str_replace("TO", file_get_contents("make.txt"), file_get_contents("bot.php"));
    file_put_contents("bots/".file_get_contents("make.txt").'/bot.php', $file);
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>"• تم صنع البوت بنجاح ؛ @$getMe->username ، 🔱
• بواسطة ؛ @username ،"
    ]);
    $webhook = file_get_contents("https://api.telegram.org/bot".file_get_contents("make.txt")."/setwebhook?url=".$_SERVER['SERVER_NAME'].'/bots/'.file_get_contents("make.txt").'/bot.php');
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>$webhook
    ]);
    unlink("make.txt");
    unlink("mode.txt");
}

if ($data == 'mak2') {
	$getMe = bot('getMe')->result;
    $file = str_replace("TO", file_get_contents("make.txt"), file_get_contents("bot2.php"));
    file_put_contents("bots/".file_get_contents("make.txt").'/bot2.php', $file);
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>"• تم صنع البوت بنجاح ؛ @$getMe->username ، 🔱
• بواسطة ؛ @username ،"
    ]);
    $webhook = file_get_contents("https://api.telegram.org/bot".file_get_contents("make.txt")."/setwebhook?url=".$_SERVER['SERVER_NAME'].'/bots/'.file_get_contents("make.txt").'/bot2.php');
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>$webhook
    ]);
    unlink("make.txt");
    unlink("mode.txt");
}

if ($data == 'mak3') {
	$getMe = bot('getMe')->result;
    $file = str_replace("TO", file_get_contents("make.txt"), file_get_contents("bot3.php"));
    file_put_contents("bots/".file_get_contents("make.txt").'/bot3.php', $file);
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>"• تم صنع البوت بنجاح ؛ @$getMe->username ، 🔱
• بواسطة ؛ @username ،"
    ]);
    $webhook = file_get_contents("https://api.telegram.org/bot".file_get_contents("make.txt")."/setwebhook?url=".$_SERVER['SERVER_NAME'].'/bots/'.file_get_contents("make.txt").'/bot3.php');
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>$webhook
    ]);
    unlink("make.txt");
    unlink("mode.txt");
}

if ($data == 'mak4') {
	$getMe = bot('getMe')->result;
    $file = str_replace("TO", file_get_contents("make.txt"), file_get_contents("bot4.php"));
    file_put_contents("bots/".file_get_contents("make.txt").'/bot4.php', $file);
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>"• تم صنع البوت بنجاح ؛ @$getMe->username ، 🔱
• بواسطة ؛ @username ،"
    ]);
    $webhook = file_get_contents("https://api.telegram.org/bot".file_get_contents("make.txt")."/setwebhook?url=".$_SERVER['SERVER_NAME'].'/bots/'.file_get_contents("make.txt").'/bot4.php');
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>$webhook
    ]);
    unlink("make.txt");
    unlink("mode.txt");
}

if ($data == 'mak5') {
	$getMe = bot('getMe')->result;
    $file = str_replace("TO", file_get_contents("make.txt"), file_get_contents("bot5.php"));
    file_put_contents("bots/".file_get_contents("make.txt").'/bot5.php', $file);
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>"• تم صنع البوت بنجاح ؛ @$getMe->username ، 🔱
• بواسطة ؛ @username ،"
    ]);
    $webhook = file_get_contents("https://api.telegram.org/bot".file_get_contents("make.txt")."/setwebhook?url=".$_SERVER['SERVER_NAME'].'/bots/'.file_get_contents("make.txt").'/bot5.php');
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>$webhook
    ]);
    unlink("make.txt");
    unlink("mode.txt");
}

if ($data == 'mak6') {
	$getMe = bot('getMe')->result;
    $file = str_replace("TO", file_get_contents("make.txt"), file_get_contents("bot6.php"));
    file_put_contents("bots/".file_get_contents("make.txt").'/bot6.php', $file);
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>"• تم صنع البوت بنجاح ؛ @$getMe->username ، 🔱
• بواسطة ؛ @username ،"
    ]);
    $webhook = file_get_contents("https://api.telegram.org/bot".file_get_contents("make.txt")."/setwebhook?url=".$_SERVER['SERVER_NAME'].'/bots/'.file_get_contents("make.txt").'/bot6.php');
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>$webhook
    ]);
    unlink("make.txt");
    unlink("mode.txt");
}

if ($data == 'mak7') {
	$getMe = bot('getMe')->result;
    $file = str_replace("TO", file_get_contents("make.txt"), file_get_contents("bot7.php"));
    file_put_contents("bots/".file_get_contents("make.txt").'/bot7.php', $file);
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>"• تم صنع البوت بنجاح ؛ @$getMe->username ، 🔱
• بواسطة ؛ @username ،"
    ]);
    $webhook = file_get_contents("https://api.telegram.org/bot".file_get_contents("make.txt")."/setwebhook?url=".$_SERVER['SERVER_NAME'].'/bots/'.file_get_contents("make.txt").'/bot7.php');
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>$webhook
    ]);
    unlink("make.txt");
    unlink("mode.txt");
}

if ($data == 'mak8') {
	$getMe = bot('getMe')->result;
    $file = str_replace("TO", file_get_contents("make.txt"), file_get_contents("bot8.php"));
    file_put_contents("bots/".file_get_contents("make.txt").'/bot8.php', $file);
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>"• تم صنع البوت بنجاح ؛ @$getMe->username ، 🔱
• بواسطة ؛ @username ،"
    ]);
    $webhook = file_get_contents("https://api.telegram.org/bot".file_get_contents("make.txt")."/setwebhook?url=".$_SERVER['SERVER_NAME'].'/bots/'.file_get_contents("make.txt").'/bot8.php');
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>$webhook
    ]);
    unlink("make.txt");
    unlink("mode.txt");
}

if ($data == 'mak9') {
	$getMe = bot('getMe')->result;
    $file = str_replace("TO", file_get_contents("make.txt"), file_get_contents("bot9.php"));
    file_put_contents("bots/".file_get_contents("make.txt").'/bot9.php', $file);
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>"• تم صنع البوت بنجاح ؛ @$getMe->username ، 🔱
• بواسطة ؛ @username ،"
    ]);
    $webhook = file_get_contents("https://api.telegram.org/bot".file_get_contents("make.txt")."/setwebhook?url=".$_SERVER['SERVER_NAME'].'/bots/'.file_get_contents("make.txt").'/bot9.php');
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>$webhook
    ]);
    unlink("make.txt");
    unlink("mode.txt");
}

if ($data == 'mak10') {
	$getMe = bot('getMe')->result;
    $file = str_replace("TO", file_get_contents("make.txt"), file_get_contents("bot10.php"));
    file_put_contents("bots/".file_get_contents("make.txt").'/bot10.php', $file);
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>"• تم صنع البوت بنجاح ؛ @$getMe->username ، 🔱
• بواسطة ؛ @username ،"
    ]);
    $webhook = file_get_contents("https://api.telegram.org/bot".file_get_contents("make.txt")."/setwebhook?url=".$_SERVER['SERVER_NAME'].'/bots/'.file_get_contents("make.txt").'/bot10.php');
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>$webhook
    ]);
    unlink("make.txt");
    unlink("mode.txt");
}

if ($data == 'mak11') {
	$getMe = bot('getMe')->result;
    $file = str_replace("TO", file_get_contents("make.txt"), file_get_contents("bot11.php"));
    file_put_contents("bots/".file_get_contents("make.txt").'/bot11.php', $file);
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>"• تم صنع البوت بنجاح ؛ @$getMe->username ، 🔱
• بواسطة ؛ @username ،"
    ]);
    $webhook = file_get_contents("https://api.telegram.org/bot".file_get_contents("make.txt")."/setwebhook?url=".$_SERVER['SERVER_NAME'].'/bots/'.file_get_contents("make.txt").'/bot11.php');
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>$webhook
    ]);
    unlink("make.txt");
    unlink("mode.txt");
}

if ($data == 'mak12') {
	$getMe = bot('getMe')->result;
    $file = str_replace("TO", file_get_contents("make.txt"), file_get_contents("bot12.php"));
    file_put_contents("bots/".file_get_contents("make.txt").'/bot12.php', $file);
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>"• تم صنع البوت بنجاح ؛ @$getMe->username ، 🔱
• بواسطة ؛ @username ،"
    ]);
    $webhook = file_get_contents("https://api.telegram.org/bot".file_get_contents("make.txt")."/setwebhook?url=".$_SERVER['SERVER_NAME'].'/bots/'.file_get_contents("make.txt").'/bot12.php');
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>$webhook
    ]);
    unlink("make.txt");
    unlink("mode.txt");
}

if ($data == 'mak13') {
	$getMe = bot('getMe')->result;
    $file = str_replace("TO", file_get_contents("make.txt"), file_get_contents("bot13.php"));
    file_put_contents("bots/".file_get_contents("make.txt").'/bot13.php', $file);
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>"• تم صنع البوت بنجاح ؛ @$getMe->username ، 🔱
• بواسطة ؛ @username ،"
    ]);
    $webhook = file_get_contents("https://api.telegram.org/bot".file_get_contents("make.txt")."/setwebhook?url=".$_SERVER['SERVER_NAME'].'/bots/'.file_get_contents("make.txt").'/bot13.php');
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>$webhook
    ]);
    unlink("make.txt");
    unlink("mode.txt");
}

if ($data == 'mak14') {
	$getMe = bot('getMe')->result;
    $file = str_replace("TO", file_get_contents("make.txt"), file_get_contents("bot14.php"));
    file_put_contents("bots/".file_get_contents("make.txt").'/bot14.php', $file);
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>"• تم صنع البوت بنجاح ؛ @$getMe->username ، 🔱
• بواسطة ؛ @username ،"
    ]);
    $webhook = file_get_contents("https://api.telegram.org/bot".file_get_contents("make.txt")."/setwebhook?url=".$_SERVER['SERVER_NAME'].'/bots/'.file_get_contents("make.txt").'/bot14.php');
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>$webhook
    ]);
    unlink("make.txt");
    unlink("mode.txt");
}

if ($data == 'mak15') {
	$getMe = bot('getMe')->result;
    $file = str_replace("TO", file_get_contents("make.txt"), file_get_contents("bot15.php"));
    file_put_contents("bots/".file_get_contents("make.txt").'/bot15.php', $file);
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>"• تم صنع البوت بنجاح ؛ @$getMe->username ، 🔱
• بواسطة ؛ @username ،"
    ]);
    $webhook = file_get_contents("https://api.telegram.org/bot".file_get_contents("make.txt")."/setwebhook?url=".$_SERVER['SERVER_NAME'].'/bots/'.file_get_contents("make.txt").'/bot15.php');
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>$webhook
    ]);
    unlink("make.txt");
    unlink("mode.txt");
}

if ($data == 'mak16') {
	$getMe = bot('getMe')->result;
    $file = str_replace("TO", file_get_contents("make.txt"), file_get_contents("bot16.php"));
    file_put_contents("bots/".file_get_contents("make.txt").'/bot16.php', $file);
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>"• تم صنع البوت بنجاح ؛ @$getMe->username ، 🔱
• بواسطة ؛ @username ،"
    ]);
    $webhook = file_get_contents("https://api.telegram.org/bot".file_get_contents("make.txt")."/setwebhook?url=".$_SERVER['SERVER_NAME'].'/bots/'.file_get_contents("make.txt").'/bot16.php');
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>$webhook
    ]);
    unlink("make.txt");
    unlink("mode.txt");
}

if ($data == 'mak17') {
	$getMe = bot('getMe')->result;
    $file = str_replace("TO", file_get_contents("make.txt"), file_get_contents("bot17.php"));
    file_put_contents("bots/".file_get_contents("make.txt").'/bot17.php', $file);
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>"• تم صنع البوت بنجاح ؛ @$getMe->username ، 🔱
• بواسطة ؛ @username ،"
    ]);
    $webhook = file_get_contents("https://api.telegram.org/bot".file_get_contents("make.txt")."/setwebhook?url=".$_SERVER['SERVER_NAME'].'/bots/'.file_get_contents("make.txt").'/bot17.php');
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>$webhook
    ]);
    unlink("make.txt");
    unlink("mode.txt");
}	

if ($data == 'mak18') {
	$getMe = bot('getMe')->result;
    $file = str_replace("TO", file_get_contents("make.txt"), file_get_contents("bot18.php"));
    file_put_contents("bots/".file_get_contents("make.txt").'/bot18.php', $file);
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>"• تم صنع البوت بنجاح ؛ @$getMe->username ، 🔱
• بواسطة ؛ @username ،"
    ]);
    $webhook = file_get_contents("https://api.telegram.org/bot".file_get_contents("make.txt")."/setwebhook?url=".$_SERVER['SERVER_NAME'].'/bots/'.file_get_contents("make.txt").'/bot18.php');
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>$webhook
    ]);
    unlink("make.txt");
    unlink("mode.txt");
}

if ($data == 'mak19') {
	$getMe = bot('getMe')->result;
    $file = str_replace("TO", file_get_contents("make.txt"), file_get_contents("bot19.php"));
    file_put_contents("bots/".file_get_contents("make.txt").'/bot19.php', $file);
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>"• تم صنع البوت بنجاح ؛ @$getMe->username ، 🔱
• بواسطة ؛ @username ،"
    ]);
    $webhook = file_get_contents("https://api.telegram.org/bot".file_get_contents("make.txt")."/setwebhook?url=".$_SERVER['SERVER_NAME'].'/bots/'.file_get_contents("make.txt").'/bot19.php');
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>$webhook
    ]);
    unlink("make.txt");
    unlink("mode.txt");
}

if ($data == 'mak20') {
	$getMe = bot('getMe')->result;
    $file = str_replace("TO", file_get_contents("make.txt"), file_get_contents("bot20.php"));
    file_put_contents("bots/".file_get_contents("make.txt").'/bot20.php', $file);
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>"• تم صنع البوت بنجاح ؛ @$getMe->username ، 🔱
• بواسطة ؛ @username ،"
    ]);
    $webhook = file_get_contents("https://api.telegram.org/bot".file_get_contents("make.txt")."/setwebhook?url=".$_SERVER['SERVER_NAME'].'/bots/'.file_get_contents("make.txt").'/bot20.php');
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>$webhook
    ]);
    unlink("make.txt");
    unlink("mode.txt");
}

if ($data == 'mak21') {
	$getMe = bot('getMe')->result;
    $file = str_replace("TO", file_get_contents("make.txt"), file_get_contents("bot21.php"));
    file_put_contents("bots/".file_get_contents("make.txt").'/bot21.php', $file);
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>"• تم صنع البوت بنجاح ؛ @$getMe->username ، 🔱
• بواسطة ؛ @username ،"
    ]);
    $webhook = file_get_contents("https://api.telegram.org/bot".file_get_contents("make.txt")."/setwebhook?url=".$_SERVER['SERVER_NAME'].'/bots/'.file_get_contents("make.txt").'/bot21.php');
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>$webhook
    ]);
    unlink("make.txt");
    unlink("mode.txt");
}

if ($data == 'mak22') {
	$getMe = bot('getMe')->result;
    $file = str_replace("TO", file_get_contents("make.txt"), file_get_contents("bot22.php"));
    file_put_contents("bots/".file_get_contents("make.txt").'/bot22.php', $file);
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>"• تم صنع البوت بنجاح ؛ @$getMe->username ، 🔱
• بواسطة ؛ @username ،"
    ]);
    $webhook = file_get_contents("https://api.telegram.org/bot".file_get_contents("make.txt")."/setwebhook?url=".$_SERVER['SERVER_NAME'].'/bots/'.file_get_contents("make.txt").'/bot22.php');
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>$webhook
    ]);
    unlink("make.txt");
    unlink("mode.txt");
}

if ($data == 'mak23') {
	$getMe = bot('getMe')->result;
    $file = str_replace("TO", file_get_contents("make.txt"), file_get_contents("bot23.php"));
    file_put_contents("bots/".file_get_contents("make.txt").'/bot.php', $file);
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>"• تم صنع البوت بنجاح ؛ @$getMe->username ، 🔱
• بواسطة ؛ @username ،"
    ]);
    $webhook = file_get_contents("https://api.telegram.org/bot".file_get_contents("make.txt")."/setwebhook?url=".$_SERVER['SERVER_NAME'].'/bots/'.file_get_contents("make.txt").'/bot23.php');
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>$webhook
    ]);
    unlink("make.txt");
    unlink("mode.txt");
}

if ($data == 'mak24') {
	$getMe = bot('getMe')->result;
    $file = str_replace("TO", file_get_contents("make.txt"), file_get_contents("bot24.php"));
    file_put_contents("bots/".file_get_contents("make.txt").'/bot24.php', $file);
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>"• تم صنع البوت بنجاح ؛ @$getMe->username ، 🔱
• بواسطة ؛ @username ،"
    ]);
    $webhook = file_get_contents("https://api.telegram.org/bot".file_get_contents("make.txt")."/setwebhook?url=".$_SERVER['SERVER_NAME'].'/bots/'.file_get_contents("make.txt").'/bot24.php');
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>$webhook
    ]);
    unlink("make.txt");
    unlink("mode.txt");
}

if ($data == 'mak25') {
	$getMe = bot('getMe')->result;
    $file = str_replace("TO", file_get_contents("make.txt"), file_get_contents("bot25.php"));
    file_put_contents("bots/".file_get_contents("make.txt").'/bot25.php', $file);
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>"• تم صنع البوت بنجاح ؛ @$getMe->username ، 🔱
• بواسطة ؛ @username ،"
    ]);
    $webhook = file_get_contents("https://api.telegram.org/bot".file_get_contents("make.txt")."/setwebhook?url=".$_SERVER['SERVER_NAME'].'/bots/'.file_get_contents("make.txt").'/bot25.php');
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>$webhook
    ]);
    unlink("make.txt");
    unlink("mode.txt");
}

if ($data == 'mak26') {
	$getMe = bot('getMe')->result;
    $file = str_replace("TO", file_get_contents("make.txt"), file_get_contents("bot26.php"));
    file_put_contents("bots/".file_get_contents("make.txt").'/bot.php', $file);
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>"• تم صنع البوت بنجاح ؛ @$getMe->username ، 🔱
• بواسطة ؛ @username ،"
    ]);
    $webhook = file_get_contents("https://api.telegram.org/bot".file_get_contents("make.txt")."/setwebhook?url=".$_SERVER['SERVER_NAME'].'/bots/'.file_get_contents("make.txt").'/bot26.php');
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>$webhook
    ]);
    unlink("make.txt");
    unlink("mode.txt");
}

if ($data == 'mak27') {
	$getMe = bot('getMe')->result;
    $file = str_replace("TO", file_get_contents("make.txt"), file_get_contents("bot27.php"));
    file_put_contents("bots/".file_get_contents("make.txt").'/bot27.php', $file);
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>"• تم صنع البوت بنجاح ؛ @$getMe->username ، 🔱
• بواسطة ؛ @username ،"
    ]);
    $webhook = file_get_contents("https://api.telegram.org/bot".file_get_contents("make.txt")."/setwebhook?url=".$_SERVER['SERVER_NAME'].'/bots/'.file_get_contents("make.txt").'/bot27.php');
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>$webhook
    ]);
    unlink("make.txt");
    unlink("mode.txt");
}

if ($data == 'mak28') {
	$getMe = bot('getMe')->result;
    $file = str_replace("TO", file_get_contents("make.txt"), file_get_contents("bot28.php"));
    file_put_contents("bots/".file_get_contents("make.txt").'/bot28.php', $file);
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>"• تم صنع البوت بنجاح ؛ @$getMe->username ، 🔱
• بواسطة ؛ @username ،"
    ]);
    $webhook = file_get_contents("https://api.telegram.org/bot".file_get_contents("make.txt")."/setwebhook?url=".$_SERVER['SERVER_NAME'].'/bots/'.file_get_contents("make.txt").'/bot28.php');
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>$webhook
    ]);
    unlink("make.txt");
    unlink("mode.txt");
}

if ($data == 'mak29') {
	$getMe = bot('getMe')->result;
    $file = str_replace("TO", file_get_contents("make.txt"), file_get_contents("bot29.php"));
    file_put_contents("bots/".file_get_contents("make.txt").'/bot29.php', $file);
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>"• تم صنع البوت بنجاح ؛ @$getMe->username ، 🔱
• بواسطة ؛ @username ،"
    ]);
    $webhook = file_get_contents("https://api.telegram.org/bot".file_get_contents("make.txt")."/setwebhook?url=".$_SERVER['SERVER_NAME'].'/bots/'.file_get_contents("make.txt").'/bot29.php');
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>$webhook
    ]);
    unlink("make.txt");
    unlink("mode.txt");
}t_id'=>$chat_id2,
        'text'=>"鈥� 鬲賲 氐賳毓 丕賱亘賵鬲 亘賳噩丕丨 貨 @$getMe->username 貙 馃敱
鈥� 亘賵丕爻胤丞 貨 @username 貙"
    ]);
    $webhook = file_get_contents("https://api.telegram.org/bot".file_get_contents("make.txt")."/setwebhook?url=".$_SERVER['SERVER_NAME'].'/bots/'.file_get_contents("make.txt").'/bot4.php');
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>$webhook
    ]);
    unlink("make.txt");
    unlink("mode.txt");
}

if ($data == 'mak5') {
	$getMe = bot('getMe')->result;
    $file = str_replace("TO", file_get_contents("make.txt"), file_get_contents("bot5.php"));
    file_put_contents("bots/".file_get_contents("make.txt").'/bot5.php', $file);
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>"鈥� 鬲賲 氐賳毓 丕賱亘賵鬲 亘賳噩丕丨 貨 @$getMe->username 貙 馃敱
鈥� 亘賵丕爻胤丞 貨 @username 貙"
    ]);
    $webhook = file_get_contents("https://api.telegram.org/bot".file_get_contents("make.txt")."/setwebhook?url=".$_SERVER['SERVER_NAME'].'/bots/'.file_get_contents("make.txt").'/bot5.php');
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>$webhook
    ]);
    unlink("make.txt");
    unlink("mode.txt");
}

if ($data == 'mak6') {
	$getMe = bot('getMe')->result;
    $file = str_replace("TO", file_get_contents("make.txt"), file_get_contents("bot6.php"));
    file_put_contents("bots/".file_get_contents("make.txt").'/bot6.php', $file);
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>"鈥� 鬲賲 氐賳毓 丕賱亘賵鬲 亘賳噩丕丨 貨 @$getMe->username 貙 馃敱
鈥� 亘賵丕爻胤丞 貨 @username 貙"
    ]);
    $webhook = file_get_contents("https://api.telegram.org/bot".file_get_contents("make.txt")."/setwebhook?url=".$_SERVER['SERVER_NAME'].'/bots/'.file_get_contents("make.txt").'/bot6.php');
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>$webhook
    ]);
    unlink("make.txt");
    unlink("mode.txt");
}

if ($data == 'mak7') {
	$getMe = bot('getMe')->result;
    $file = str_replace("TO", file_get_contents("make.txt"), file_get_contents("bot7.php"));
    file_put_contents("bots/".file_get_contents("make.txt").'/bot7.php', $file);
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>"鈥� 鬲賲 氐賳毓 丕賱亘賵鬲 亘賳噩丕丨 貨 @$getMe->username 貙 馃敱
鈥� 亘賵丕爻胤丞 貨 @username 貙"
    ]);
    $webhook = file_get_contents("https://api.telegram.org/bot".file_get_contents("make.txt")."/setwebhook?url=".$_SERVER['SERVER_NAME'].'/bots/'.file_get_contents("make.txt").'/bot7.php');
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>$webhook
    ]);
    unlink("make.txt");
    unlink("mode.txt");
}

if ($data == 'mak8') {
	$getMe = bot('getMe')->result;
    $file = str_replace("TO", file_get_contents("make.txt"), file_get_contents("bot8.php"));
    file_put_contents("bots/".file_get_contents("make.txt").'/bot8.php', $file);
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>"鈥� 鬲賲 氐賳毓 丕賱亘賵鬲 亘賳噩丕丨 貨 @$getMe->username 貙 馃敱
鈥� 亘賵丕爻胤丞 貨 @username 貙"
    ]);
    $webhook = file_get_contents("https://api.telegram.org/bot".file_get_contents("make.txt")."/setwebhook?url=".$_SERVER['SERVER_NAME'].'/bots/'.file_get_contents("make.txt").'/bot8.php');
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>$webhook
    ]);
    unlink("make.txt");
    unlink("mode.txt");
}

if ($data == 'mak9') {
	$getMe = bot('getMe')->result;
    $file = str_replace("TO", file_get_contents("make.txt"), file_get_contents("bot9.php"));
    file_put_contents("bots/".file_get_contents("make.txt").'/bot9.php', $file);
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>"鈥� 鬲賲 氐賳毓 丕賱亘賵鬲 亘賳噩丕丨 貨 @$getMe->username 貙 馃敱
鈥� 亘賵丕爻胤丞 貨 @username 貙"
    ]);
    $webhook = file_get_contents("https://api.telegram.org/bot".file_get_contents("make.txt")."/setwebhook?url=".$_SERVER['SERVER_NAME'].'/bots/'.file_get_contents("make.txt").'/bot9.php');
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>$webhook
    ]);
    unlink("make.txt");
    unlink("mode.txt");
}

if ($data == 'mak10') {
	$getMe = bot('getMe')->result;
    $file = str_replace("TO", file_get_contents("make.txt"), file_get_contents("bot10.php"));
    file_put_contents("bots/".file_get_contents("make.txt").'/bot10.php', $file);
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>"鈥� 鬲賲 氐賳毓 丕賱亘賵鬲 亘賳噩丕丨 貨 @$getMe->username 貙 馃敱
鈥� 亘賵丕爻胤丞 貨 @username 貙"
    ]);
    $webhook = file_get_contents("https://api.telegram.org/bot".file_get_contents("make.txt")."/setwebhook?url=".$_SERVER['SERVER_NAME'].'/bots/'.file_get_contents("make.txt").'/bot10.php');
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>$webhook
    ]);
    unlink("make.txt");
    unlink("mode.txt");
}

if ($data == 'mak11') {
	$getMe = bot('getMe')->result;
    $file = str_replace("TO", file_get_contents("make.txt"), file_get_contents("bot11.php"));
    file_put_contents("bots/".file_get_contents("make.txt").'/bot11.php', $file);
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>"鈥� 鬲賲 氐賳毓 丕賱亘賵鬲 亘賳噩丕丨 貨 @$getMe->username 貙 馃敱
鈥� 亘賵丕爻胤丞 貨 @username 貙"
    ]);
    $webhook = file_get_contents("https://api.telegram.org/bot".file_get_contents("make.txt")."/setwebhook?url=".$_SERVER['SERVER_NAME'].'/bots/'.file_get_contents("make.txt").'/bot11.php');
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>$webhook
    ]);
    unlink("make.txt");
    unlink("mode.txt");
}

if ($data == 'mak12') {
	$getMe = bot('getMe')->result;
    $file = str_replace("TO", file_get_contents("make.txt"), file_get_contents("bot12.php"));
    file_put_contents("bots/".file_get_contents("make.txt").'/bot12.php', $file);
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>"鈥� 鬲賲 氐賳毓 丕賱亘賵鬲 亘賳噩丕丨 貨 @$getMe->username 貙 馃敱
鈥� 亘賵丕爻胤丞 貨 @username 貙"
    ]);
    $webhook = file_get_contents("https://api.telegram.org/bot".file_get_contents("make.txt")."/setwebhook?url=".$_SERVER['SERVER_NAME'].'/bots/'.file_get_contents("make.txt").'/bot12.php');
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>$webhook
    ]);
    unlink("make.txt");
    unlink("mode.txt");
}

if ($data == 'mak13') {
	$getMe = bot('getMe')->result;
    $file = str_replace("TO", file_get_contents("make.txt"), file_get_contents("bot13.php"));
    file_put_contents("bots/".file_get_contents("make.txt").'/bot13.php', $file);
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>"鈥� 鬲賲 氐賳毓 丕賱亘賵鬲 亘賳噩丕丨 貨 @$getMe->username 貙 馃敱
鈥� 亘賵丕爻胤丞 貨 @username 貙"
    ]);
    $webhook = file_get_contents("https://api.telegram.org/bot".file_get_contents("make.txt")."/setwebhook?url=".$_SERVER['SERVER_NAME'].'/bots/'.file_get_contents("make.txt").'/bot13.php');
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>$webhook
    ]);
    unlink("make.txt");
    unlink("mode.txt");
}

if ($data == 'mak14') {
	$getMe = bot('getMe')->result;
    $file = str_replace("TO", file_get_contents("make.txt"), file_get_contents("bot14.php"));
    file_put_contents("bots/".file_get_contents("make.txt").'/bot14.php', $file);
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>"鈥� 鬲賲 氐賳毓 丕賱亘賵鬲 亘賳噩丕丨 貨 @$getMe->username 貙 馃敱
鈥� 亘賵丕爻胤丞 貨 @username 貙"
    ]);
    $webhook = file_get_contents("https://api.telegram.org/bot".file_get_contents("make.txt")."/setwebhook?url=".$_SERVER['SERVER_NAME'].'/bots/'.file_get_contents("make.txt").'/bot14.php');
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>$webhook
    ]);
    unlink("make.txt");
    unlink("mode.txt");
}

if ($data == 'mak15') {
	$getMe = bot('getMe')->result;
    $file = str_replace("TO", file_get_contents("make.txt"), file_get_contents("bot15.php"));
    file_put_contents("bots/".file_get_contents("make.txt").'/bot15.php', $file);
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>"鈥� 鬲賲 氐賳毓 丕賱亘賵鬲 亘賳噩丕丨 貨 @$getMe->username 貙 馃敱
鈥� 亘賵丕爻胤丞 貨 @username 貙"
    ]);
    $webhook = file_get_contents("https://api.telegram.org/bot".file_get_contents("make.txt")."/setwebhook?url=".$_SERVER['SERVER_NAME'].'/bots/'.file_get_contents("make.txt").'/bot15.php');
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>$webhook
    ]);
    unlink("make.txt");
    unlink("mode.txt");
}

if ($data == 'mak16') {
	$getMe = bot('getMe')->result;
    $file = str_replace("TO", file_get_contents("make.txt"), file_get_contents("bot16.php"));
    file_put_contents("bots/".file_get_contents("make.txt").'/bot16.php', $file);
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>"鈥� 鬲賲 氐賳毓 丕賱亘賵鬲 亘賳噩丕丨 貨 @$getMe->username 貙 馃敱
鈥� 亘賵丕爻胤丞 貨 @username 貙"
    ]);
    $webhook = file_get_contents("https://api.telegram.org/bot".file_get_contents("make.txt")."/setwebhook?url=".$_SERVER['SERVER_NAME'].'/bots/'.file_get_contents("make.txt").'/bot16.php');
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>$webhook
    ]);
    unlink("make.txt");
    unlink("mode.txt");
}

if ($data == 'mak17') {
	$getMe = bot('getMe')->result;
    $file = str_replace("TO", file_get_contents("make.txt"), file_get_contents("bot17.php"));
    file_put_contents("bots/".file_get_contents("make.txt").'/bot17.php', $file);
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>"鈥� 鬲賲 氐賳毓 丕賱亘賵鬲 亘賳噩丕丨 貨 @$getMe->username 貙 馃敱
鈥� 亘賵丕爻胤丞 貨 @username 貙"
    ]);
    $webhook = file_get_contents("https://api.telegram.org/bot".file_get_contents("make.txt")."/setwebhook?url=".$_SERVER['SERVER_NAME'].'/bots/'.file_get_contents("make.txt").'/bot17.php');
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>$webhook
    ]);
    unlink("make.txt");
    unlink("mode.txt");
}	

if ($data == 'mak18') {
	$getMe = bot('getMe')->result;
    $file = str_replace("TO", file_get_contents("make.txt"), file_get_contents("bot18.php"));
    file_put_contents("bots/".file_get_contents("make.txt").'/bot18.php', $file);
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>"鈥� 鬲賲 氐賳毓 丕賱亘賵鬲 亘賳噩丕丨 貨 @$getMe->username 貙 馃敱
鈥� 亘賵丕爻胤丞 貨 @username 貙"
    ]);
    $webhook = file_get_contents("https://api.telegram.org/bot".file_get_contents("make.txt")."/setwebhook?url=".$_SERVER['SERVER_NAME'].'/bots/'.file_get_contents("make.txt").'/bot18.php');
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>$webhook
    ]);
    unlink("make.txt");
    unlink("mode.txt");
}

if ($data == 'mak19') {
	$getMe = bot('getMe')->result;
    $file = str_replace("TO", file_get_contents("make.txt"), file_get_contents("bot19.php"));
    file_put_contents("bots/".file_get_contents("make.txt").'/bot19.php', $file);
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>"鈥� 鬲賲 氐賳毓 丕賱亘賵鬲 亘賳噩丕丨 貨 @$getMe->username 貙 馃敱
鈥� 亘賵丕爻胤丞 貨 @username 貙"
    ]);
    $webhook = file_get_contents("https://api.telegram.org/bot".file_get_contents("make.txt")."/setwebhook?url=".$_SERVER['SERVER_NAME'].'/bots/'.file_get_contents("make.txt").'/bot19.php');
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>$webhook
    ]);
    unlink("make.txt");
    unlink("mode.txt");
}

if ($data == 'mak20') {
	$getMe = bot('getMe')->result;
    $file = str_replace("TO", file_get_contents("make.txt"), file_get_contents("bot20.php"));
    file_put_contents("bots/".file_get_contents("make.txt").'/bot20.php', $file);
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>"鈥� 鬲賲 氐賳毓 丕賱亘賵鬲 亘賳噩丕丨 貨 @$getMe->username 貙 馃敱
鈥� 亘賵丕爻胤丞 貨 @username 貙"
    ]);
    $webhook = file_get_contents("https://api.telegram.org/bot".file_get_contents("make.txt")."/setwebhook?url=".$_SERVER['SERVER_NAME'].'/bots/'.file_get_contents("make.txt").'/bot20.php');
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>$webhook
    ]);
    unlink("make.txt");
    unlink("mode.txt");
}

if ($data == 'mak21') {
	$getMe = bot('getMe')->result;
    $file = str_replace("TO", file_get_contents("make.txt"), file_get_contents("bot21.php"));
    file_put_contents("bots/".file_get_contents("make.txt").'/bot21.php', $file);
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>"鈥� 鬲賲 氐賳毓 丕賱亘賵鬲 亘賳噩丕丨 貨 @$getMe->username 貙 馃敱
鈥� 亘賵丕爻胤丞 貨 @username 貙"
    ]);
    $webhook = file_get_contents("https://api.telegram.org/bot".file_get_contents("make.txt")."/setwebhook?url=".$_SERVER['SERVER_NAME'].'/bots/'.file_get_contents("make.txt").'/bot21.php');
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>$webhook
    ]);
    unlink("make.txt");
    unlink("mode.txt");
}

if ($data == 'mak22') {
	$getMe = bot('getMe')->result;
    $file = str_replace("TO", file_get_contents("make.txt"), file_get_contents("bot22.php"));
    file_put_contents("bots/".file_get_contents("make.txt").'/bot22.php', $file);
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>"鈥� 鬲賲 氐賳毓 丕賱亘賵鬲 亘賳噩丕丨 貨 @$getMe->username 貙 馃敱
鈥� 亘賵丕爻胤丞 貨 @username 貙"
    ]);
    $webhook = file_get_contents("https://api.telegram.org/bot".file_get_contents("make.txt")."/setwebhook?url=".$_SERVER['SERVER_NAME'].'/bots/'.file_get_contents("make.txt").'/bot22.php');
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>$webhook
    ]);
    unlink("make.txt");
    unlink("mode.txt");
}

if ($data == 'mak23') {
	$getMe = bot('getMe')->result;
    $file = str_replace("TO", file_get_contents("make.txt"), file_get_contents("bot23.php"));
    file_put_contents("bots/".file_get_contents("make.txt").'/bot.php', $file);
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>"鈥� 鬲賲 氐賳毓 丕賱亘賵鬲 亘賳噩丕丨 貨 @$getMe->username 貙 馃敱
鈥� 亘賵丕爻胤丞 貨 @username 貙"
    ]);
    $webhook = file_get_contents("https://api.telegram.org/bot".file_get_contents("make.txt")."/setwebhook?url=".$_SERVER['SERVER_NAME'].'/bots/'.file_get_contents("make.txt").'/bot23.php');
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>$webhook
    ]);
    unlink("make.txt");
    unlink("mode.txt");
}

if ($data == 'mak24') {
	$getMe = bot('getMe')->result;
    $file = str_replace("TO", file_get_contents("make.txt"), file_get_contents("bot24.php"));
    file_put_contents("bots/".file_get_contents("make.txt").'/bot24.php', $file);
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>"鈥� 鬲賲 氐賳毓 丕賱亘賵鬲 亘賳噩丕丨 貨 @$getMe->username 貙 馃敱
鈥� 亘賵丕爻胤丞 貨 @username 貙"
    ]);
    $webhook = file_get_contents("https://api.telegram.org/bot".file_get_contents("make.txt")."/setwebhook?url=".$_SERVER['SERVER_NAME'].'/bots/'.file_get_contents("make.txt").'/bot24.php');
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>$webhook
    ]);
    unlink("make.txt");
    unlink("mode.txt");
}

if ($data == 'mak25') {
	$getMe = bot('getMe')->result;
    $file = str_replace("TO", file_get_contents("make.txt"), file_get_contents("bot25.php"));
    file_put_contents("bots/".file_get_contents("make.txt").'/bot25.php', $file);
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>"鈥� 鬲賲 氐賳毓 丕賱亘賵鬲 亘賳噩丕丨 貨 @$getMe->username 貙 馃敱
鈥� 亘賵丕爻胤丞 貨 @username 貙"
    ]);
    $webhook = file_get_contents("https://api.telegram.org/bot".file_get_contents("make.txt")."/setwebhook?url=".$_SERVER['SERVER_NAME'].'/bots/'.file_get_contents("make.txt").'/bot25.php');
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>$webhook
    ]);
    unlink("make.txt");
    unlink("mode.txt");
}

if ($data == 'mak26') {
	$getMe = bot('getMe')->result;
    $file = str_replace("TO", file_get_contents("make.txt"), file_get_contents("bot26.php"));
    file_put_contents("bots/".file_get_contents("make.txt").'/bot.php', $file);
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>"鈥� 鬲賲 氐賳毓 丕賱亘賵鬲 亘賳噩丕丨 貨 @$getMe->username 貙 馃敱
鈥� 亘賵丕爻胤丞 貨 @username 貙"
    ]);
    $webhook = file_get_contents("https://api.telegram.org/bot".file_get_contents("make.txt")."/setwebhook?url=".$_SERVER['SERVER_NAME'].'/bots/'.file_get_contents("make.txt").'/bot26.php');
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>$webhook
    ]);
    unlink("make.txt");
    unlink("mode.txt");
}

if ($data == 'mak27') {
	$getMe = bot('getMe')->result;
    $file = str_replace("TO", file_get_contents("make.txt"), file_get_contents("bot27.php"));
    file_put_contents("bots/".file_get_contents("make.txt").'/bot27.php', $file);
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>"鈥� 鬲賲 氐賳毓 丕賱亘賵鬲 亘賳噩丕丨 貨 @$getMe->username 貙 馃敱
鈥� 亘賵丕爻胤丞 貨 @username 貙"
    ]);
    $webhook = file_get_contents("https://api.telegram.org/bot".file_get_contents("make.txt")."/setwebhook?url=".$_SERVER['SERVER_NAME'].'/bots/'.file_get_contents("make.txt").'/bot27.php');
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>$webhook
    ]);
    unlink("make.txt");
    unlink("mode.txt");
}

if ($data == 'mak28') {
	$getMe = bot('getMe')->result;
    $file = str_replace("TO", file_get_contents("make.txt"), file_get_contents("bot28.php"));
    file_put_contents("bots/".file_get_contents("make.txt").'/bot28.php', $file);
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>"鈥� 鬲賲 氐賳毓 丕賱亘賵鬲 亘賳噩丕丨 貨 @$getMe->username 貙 馃敱
鈥� 亘賵丕爻胤丞 貨 @username 貙"
    ]);
    $webhook = file_get_contents("https://api.telegram.org/bot".file_get_contents("make.txt")."/setwebhook?url=".$_SERVER['SERVER_NAME'].'/bots/'.file_get_contents("make.txt").'/bot28.php');
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>$webhook
    ]);
    unlink("make.txt");
    unlink("mode.txt");
}

if ($data == 'mak29') {
	$getMe = bot('getMe')->result;
    $file = str_replace("TO", file_get_contents("make.txt"), file_get_contents("bot29.php"));
    file_put_contents("bots/".file_get_contents("make.txt").'/bot29.php', $file);
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>"鈥� 鬲賲 氐賳毓 丕賱亘賵鬲 亘賳噩丕丨 貨 @$getMe->username 貙 馃敱
鈥� 亘賵丕爻胤丞 貨 @username 貙"
    ]);
    $webhook = file_get_contents("https://api.telegram.org/bot".file_get_contents("make.txt")."/setwebhook?url=".$_SERVER['SERVER_NAME'].'/bots/'.file_get_contents("make.txt").'/bot29.php');
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>$webhook
    ]);
    unlink("make.txt");
    unlink("mode.txt");
}