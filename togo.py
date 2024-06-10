 <?php
$API_KEY = '6499198312:AAG1VAJHQ9pf0XD7UHA2Em5zXhisPxkgwe8'; // 1„21‡21†71‡0
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
$admin = 5099564264; /*1ƒ91‡41„71‡4 1ƒ91†81†91…51‡21„9*/
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
            'text'=>"- 1ƒ91‡11†81ƒ9 1„01†7 1‡41ƒ9 ”9Ð9”9È91‚7 [$name](tg://user?id=$chat_id) 12
©m©m©m©m©m©m©m©m©m©m©m©m

- 1†51‡4 1„01‡21„2 1…31‡01…7 1„01‡21„21ƒ91„2 1ƒ91†81†71„21ƒ91„01„1 1ƒ91†81„61ƒ91…3 1„01†7 12 ”9á0'
- 1†61†9 1„01…31‡01…7 1ƒ91†81„01‡21„2 1ƒ91†81„81‡4 1„21„91‡41„71‡1 1ƒ91†81ƒ91‡0 12 ”9°6'
- 1†91…7 1†91‡41…01„1 1„21…81‡41‡41„9 1ƒ91†81„51†61‡21†6 1†91‡0 1ƒ91†81„01‡21„2 12 ”9Ý8'
- 1†91†81ƒ91„51…61„1 1‚7 1†81ƒ9 1‡41†91†71‡0 1†81…81‡41„91†7 1ƒ91‡0 1‡41…31‡01…7 1„01‡21„2 12 ”9”4”9•2'
- 1‡11„81ƒ9 1ƒ91†81„01‡21„2 1„61ƒ91…3 1„01ƒ91†81†91…51‡21„9 1†51†61…5 12 7±5'
©m©m©m©m©m©m©m©m©m©m©m©m",
            'reply_markup'=>json_encode([
                'inline_keyboard'=>[
                    [['text'=>'6¦1 1…31‡01…7 1„01‡21„2 12 7Â9„1‚5 6¦1','callback_data'=>"make"],['text'=>'1„51„81†5 1„01‡21„2 ','callback_data'=>'del']],
                   [['text'=>"- By 1‚7", "callback_data"=>"zhaemr"],['text'=>"@$username .", "callback_data"=>"zhaemr"]], 
                ]
            ])
        ]);
    } else {
        bot('sendmessage',[
            'chat_id'=>$chat_id,
            'text'=>"6¦1 1ƒ91†81‡41†7 1†61ƒ91ƒ81†91„11‡1 1„21…81‡41‡41„9 1„51†61‡21†6 1ƒ91†81„01‡21„2 12 ”9ç8
6¦1 1†61†9 1„01„21…81‡41‡41„9 1†91ƒ91„21„91‡41„7 1…71‡01„7 1ƒ91†81ƒ91‡01„21‡11ƒ91ƒ3 1ƒ91…41…81…5 1…71†81‡3 1…01„9 1…31‡01…7 1ƒ91†81„01‡21„2 12 ”9à0
©m©m©m©m©m©m©m©m©m©m©m©m",
            'reply_markup'=>json_encode([
                'inline_keyboard'=>[
                    [['text'=>'6¦1 1„21…71„71‡41†8 1ƒ91‡41„71‡4 1ƒ91†81†91…51‡21„9 12 ”9å3','callback_data'=>"setid"]],
                    [['text'=>'6¦1 1„21…71„71‡41†8 1†91…71„91†5 1ƒ91†81†61‡01ƒ91„1 12 ”9°6','callback_data'=>"setch"]],
                    [['text'=>'6¦1 1„21…71„71‡41†8 1…01„9 1†81…21„91ƒ91ƒ3 1ƒ91†81„01‡21„2 12 7²2„1‚5','callback_data'=>"setbuy"]],
                    [['text'=>"6¦1 1…31‡01…7 1ƒ91†81„01‡21„2 12 ”9Ý8",'callback_data'=>'se']]
                ]
            ])
        ]);
    }
}
if($data == 'del'){
    bot('editMessageText',[
       'chat_id'=>$chat_id2,
       'message_id'=>$message_id,
       'text'=>'1ƒ91„91…11†8 1ƒ91†81„21‡21†71‡0'
    ]);
    file_put_contents('mode.txt','del');
}
if ($data == 'make') {
    bot('sendmessage',[
            'chat_id'=>$chat_id2,
            'text'=>"6¦1 1ƒ91†81ƒ91‡0 1†61†9 1„01ƒ91„91…11ƒ91†8 1„21‡21†71‡0 1ƒ91†81„01‡21„2 12 7¤1„1‚5
6¦1 1†61†9 1„01„41†81„0 1ƒ91†81„21‡21†71‡0 1†91‡0 @BotFather 12 ”9á2
©m©m©m©m©m©m©m©m©m©m©m©m",
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
            'text'=>"6¦1 1ƒ91†81‡41†7 1†61ƒ91ƒ81†91„11‡1 1„21…81‡41‡41„9 1„51†61‡21†6 1ƒ91†81„01‡21„2 12 ”9ç8
6¦1 1†61†9 1„01„21…81‡41‡41„9 1†91ƒ91„21„91‡41„7 1…71‡01„7 1ƒ91†81ƒ91‡01„21‡11ƒ91ƒ3 1ƒ91…41…81…5 1…71†81‡3 1…01„9 1…31‡01…7 1ƒ91†81„01‡21„2 12 ”9à0
©m©m©m©m©m©m©m©m©m©m©m©m",
            'reply_markup'=>json_encode([
                'inline_keyboard'=>[
                    [['text'=>'6¦1 1„21…71„71‡41†8 1ƒ91‡41„71‡4 1ƒ91†81†91…51‡21„9 12 ”9å3','callback_data'=>"setid"]],
                    [['text'=>'6¦1 1„21…71„71‡41†8 1†91…71„91†5 1ƒ91†81†61‡01ƒ91„1 12 ”9°6','callback_data'=>"setch"]],
                    [['text'=>'6¦1 1„21…71„71‡41†8 1…01„9 1†81…21„91ƒ91ƒ3 1ƒ91†81„01‡21„2 12 7²2„1‚5','callback_data'=>"setbuy"]],
                    [['text'=>"6¦1 1…31‡01…7 1ƒ91†81„01‡21„2 12 ”9Ý8",'callback_data'=>'se']]
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
       'text'=>"- 1ƒ91„61„21„9 1ƒ91†81„01‡21„2 1ƒ91†81„81‡4 1„21‡21„7 1…31‡01…71‡1 ; ”9ç9 !",
       'reply_markup'=>json_encode([
                'inline_keyboard'=>[	
                [['text'=>"6¦1 1„01‡21„2 1…01„61„91†51„11‡1 12 7±2 1‚7",'callback_data'=>'mak'],['text'=>"6¦1 1„01‡21„2 1ƒ91†81ƒ91†81…71ƒ91„0 12 ”9Á2 1‚7",'callback_data'=>'mak2']],
                    [['text'=>"6¦1 1„01‡21„2 1ƒ91†81„61‡41„91„1 12 ”9â9 1‚7",'callback_data'=>'mak3'],['text'=>"6¦1 1†61„91ƒ91ƒ31„1 1ƒ91†81†71†5 12 ”9ê4 1‚7",'callback_data'=>'mak4']],
                    [['text'=>"6¦1 1ƒ91†81„51‡21„2 1ƒ91†81ƒ91…01„91†6 12 ”9Í8 1‚7",'callback_data'=>'mak5'],['text'=>"6¦1 1†81…71„01„1 1ƒ91†71…1 1ƒ91‡2 12 ”9½8 1‚7",'callback_data'=>'mak6']],
                    [['text'=>"6¦1 1…31‡01…7 1„01ƒ91‡41‡2 12 9¦3„1‚5 1‚7",'callback_data'=>'mak7'],['text'=>"6¦1 1…31‡01…7 1†91„21„51„91†71‡1 12 ”9½2 1‚7",'callback_data'=>'mak8']],
                    [['text'=>"6¦1 1„21„91„21‡41„0 1ƒ91†81†71†81ƒ91†9 12 ”9”4”9•2 1‚7",'callback_data'=>'mak9'],['text'=>"6¦1 1†81‡2 1„61‡41„91‡21†7 12 ”9°6 1‚7",'callback_data'=>'mak10']],
                    [['text'=>"6¦1 1ƒ91†81…71„01ƒ91„91ƒ91„2 1ƒ91†81„41„71ƒ91„91‡41„1 12 ”9¶6 1‚7",'callback_data'=>'mak11'],['text'=>"6¦1 1„01‡21„2 1ƒ91†81ƒ91„01„91ƒ91„4 12 ”9Î5 1‚7",'callback_data'=>'mak12']],
                    [['text'=>"6¦1 1„51…01‡21„91„1 1„01†81‡41„91„1 12 •05 1‚7",'callback_data'=>'mak13'],['text'=>"6¦1 1†71„21ƒ91„01„1 1…7 1…31‡21„9 12 ”9½3 1‚7",'callback_data'=>'mak14']],
                    [['text'=>"6¦1 1„01‡21„2 1ƒ91†81†91„51‡41„01…1 12 7¼8”9È9 1‚7",'callback_data'=>'mak15'],['text'=>"6¦1 1…01‡41ƒ91„71„1 1ƒ91†81ƒ91…71…41ƒ91ƒ3 12 ”9á0 1‚7",'callback_data'=>'mak16']],
                    [['text'=>"6¦1 1„21„51†91‡41†8 1†91‡0 1†91‡41‡21…01†71†81‡4 12 7‘4„1‚5 1‚7",'callback_data'=>'mak17']],
                    [['text'=>"6¦1 1„21„51†91‡41†8 1†91‡0 1ƒ91†81ƒ91‡01…11„21ƒ9 12 ”9â7 1‚7",'callback_data'=>'mak18']],
                    [['text'=>"6¦1 1„21„51†91‡41†8 1†91‡0 1ƒ91†81‡41‡21„21‡41‡21„0 12 ”9Þ7 1‚7",'callback_data'=>'mak19']],
                    [['text'=>"6¦1 1„01‡21„2 1ƒ91†81„91…31‡41„7 12 ”9Û6 1‚7",'callback_data'=>'mak20'],['text'=>"6¦1 1„51†91ƒ91‡41„11‡1 1†61‡01‡21ƒ91„2 12 •0•11‚7",'callback_data'=>'mak21']],
                    [['text'=>"6¦1 1„01‡21„2 1ƒ91†81„21…51„01‡41†61ƒ91„2 12 •0“6 1‚7",'callback_data'=>'mak22'],['text'=>"6¦1 1„01‡21„2 1ƒ91†81†51‡21„21‡21…21‡21„0 12 ”9Ý3 1‚7",'callback_data'=>'mak23']],
                    [['text'=>"6¦1 1„01‡21„2 1ƒ91†81ƒ91„91†61ƒ91†9 12 ”9ç6 1‚7",'callback_data'=>'mak24'],['text'=>"6¦1 1„01‡21„2 1ƒ91‡11†91…11†81‡4 12 ”9Ú6 1‚7",'callback_data'=>'mak25']],
                    [['text'=>"6¦1 1†51‡41„71‡41‡2 1ƒ91‡01…11„21ƒ9 12 ”9Ù6 1‚7",'callback_data'=>'mak26'],['text'=>"6¦1 1„01‡21„2 1ƒ91†81†91‡21ƒ91…31†51ƒ91„2 12 ”9²9 1‚7",'callback_data'=>'mak27']],
                    [['text'=>"6¦1 1‡11†8 1„21…71†81†9 12 7Ä31‚7",'callback_data'=>'mak28'],['text'=>"6¦1 1„01‡21„2 1ƒ91†81„61†81†51‡41ƒ91„2 12 ”9á2 1‚7",'callback_data'=>'mak29']],
                    [['text'=>"- Saad Mohammed ; ”9ç9 !!",'url'=>'t.me/sssbs']],
                        ]
            ])
        ]);
    }
    
if ($data == 'setid') {
    file_put_contents("mode.txt", "ids");
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>"1„71…0 1ƒ91†81ƒ91‡41„71‡4"
    ]);
}
if($text and file_get_contents('mode.txt') == 'del'){
    if(is_dir('bots/'.$text)){
        $sc = scandir('bots/'.$text);
        foreach($sc as $k => $v){
            unlink('bots/'.$text.'/'.$v);
        }
        rmdir('bots/'.$text);
        bot('sendMessage',['chat_id'=>$chat_id,'text'=>'1„21†9 1ƒ91†81„51„81†5']);
    } else {
        bot('sendmessage',['chat_id'=>$chat_id,'text'=>'1†81†9 1‡41„21†9 1…31‡01…7 1ƒ91‡4 1„01‡21„2 1„01‡11„81ƒ9 1ƒ91†81„21‡21†71‡0']);
    }
    unlink('mode.txt');
}
elseif(preg_match('/[0-9]/',$text)  and file_get_contents("mode.txt") == 'ids') {
        file_put_contents("bots/".file_get_contents("make.txt").'/ids.txt', $text);

    bot('sendmessage',[
            'chat_id'=>$chat_id,
            'text'=>"6¦1 1ƒ91†81‡41†7 1†61ƒ91ƒ81†91„11‡1 1„21…81‡41‡41„9 1„51†61‡21†6 1ƒ91†81„01‡21„2 12 ”9ç8
6¦1 1†61†9 1„01„21…81‡41‡41„9 1†91ƒ91„21„91‡41„7 1…71‡01„7 1ƒ91†81ƒ91‡01„21‡11ƒ91ƒ3 1ƒ91…41…81…5 1…71†81‡3 1…01„9 1…31‡01…7 1ƒ91†81„01‡21„2 12 ”9à0
©m©m©m©m©m©m©m©m©m©m©m©m",
            'reply_markup'=>json_encode([
                'inline_keyboard'=>[
                    [['text'=>'6¦1 1„21…71„71‡41†8 1ƒ91‡41„71‡4 1ƒ91†81†91…51‡21„9 12 ”9å3','callback_data'=>"setid"]],
                    [['text'=>'6¦1 1„21…71„71‡41†8 1†91…71„91†5 1ƒ91†81†61‡01ƒ91„1 12 ”9°6','callback_data'=>"setch"]],
                    [['text'=>'6¦1 1„21…71„71‡41†8 1…01„9 1†81…21„91ƒ91ƒ3 1ƒ91†81„01‡21„2 12 7²2„1‚5','callback_data'=>"setbuy"]],
                    [['text'=>"6¦1 1…31‡01…7 1ƒ91†81„01‡21„2 12 ”9Ý8",'callback_data'=>'se']]
                ]
            ])
        ]);
        file_put_contents("mode.txt", "..");
}

if ($data == 'setch') {
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>"1„71…0 1ƒ91†81†61‡01ƒ91‡1"
    ]);
    file_put_contents("mode.txt", "ch");
}
elseif($text and file_get_contents("mode.txt") == 'ch') {
        file_put_contents("bots/".file_get_contents("make.txt").'/ch.txt', $text);

    bot('sendmessage',[
            'chat_id'=>$chat_id,
            'text'=>"6¦1 1ƒ91†81‡41†7 1†61ƒ91ƒ81†91„11‡1 1„21…81‡41‡41„9 1„51†61‡21†6 1ƒ91†81„01‡21„2 12 ”9ç8
6¦1 1†61†9 1„01„21…81‡41‡41„9 1†91ƒ91„21„91‡41„7 1…71‡01„7 1ƒ91†81ƒ91‡01„21‡11ƒ91ƒ3 1ƒ91…41…81…5 1…71†81‡3 1…01„9 1…31‡01…7 1ƒ91†81„01‡21„2 12 ”9à0
©m©m©m©m©m©m©m©m©m©m©m©m",
            'reply_markup'=>json_encode([
                'inline_keyboard'=>[
                    [['text'=>'6¦1 1„21…71„71‡41†8 1ƒ91‡41„71‡4 1ƒ91†81†91…51‡21„9 12 ”9å3','callback_data'=>"setid"]],
                    [['text'=>'6¦1 1„21…71„71‡41†8 1†91…71„91†5 1ƒ91†81†61‡01ƒ91„1 12 ”9°6','callback_data'=>"setch"]],
                    [['text'=>'6¦1 1„21…71„71‡41†8 1…01„9 1†81…21„91ƒ91ƒ3 1ƒ91†81„01‡21„2 12 7²2„1‚5','callback_data'=>"setbuy"]],
                    [['text'=>"6¦1 1…31‡01…7 1ƒ91†81„01‡21„2 12 ”9Ý8",'callback_data'=>'se']]
                ]
            ])
        ]);
        file_put_contents("mode.txt", "..");
}
if ($data == 'setbuy') {
    file_put_contents("mode.txt", "buy");
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>"1„71…0 1ƒ91†81†91…71„91†5"
    ]);
}
elseif($text  and file_get_contents("mode.txt") == 'buy') {
        file_put_contents("bots/".file_get_contents("make.txt").'/buy.txt', $text);

    bot('sendmessage',[
            'chat_id'=>$chat_id,
            'text'=>"6¦1 1ƒ91†81‡41†7 1†61ƒ91ƒ81†91„11‡1 1„21…81‡41‡41„9 1„51†61‡21†6 1ƒ91†81„01‡21„2 12 ”9ç8
6¦1 1†61†9 1„01„21…81‡41‡41„9 1†91ƒ91„21„91‡41„7 1…71‡01„7 1ƒ91†81ƒ91‡01„21‡11ƒ91ƒ3 1ƒ91…41…81…5 1…71†81‡3 1…01„9 1…31‡01…7 1ƒ91†81„01‡21„2 12 ”9à0
©m©m©m©m©m©m©m©m©m©m©m©m",
            'reply_markup'=>json_encode([
                'inline_keyboard'=>[
                    [['text'=>'6¦1 1„21…71„71‡41†8 1ƒ91‡41„71‡4 1ƒ91†81†91…51‡21„9 12 ”9å3','callback_data'=>"setid"]],
                    [['text'=>'6¦1 1„21…71„71‡41†8 1†91…71„91†5 1ƒ91†81†61‡01ƒ91„1 12 ”9°6','callback_data'=>"setch"]],
                    [['text'=>'6¦1 1„21…71„71‡41†8 1…01„9 1†81…21„91ƒ91ƒ3 1ƒ91†81„01‡21„2 12 7²2„1‚5','callback_data'=>"setbuy"]],
                    [['text'=>"6¦1 1…31‡01…7 1ƒ91†81„01‡21„2 12 ”9Ý8",'callback_data'=>'se']]
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
        'text'=>"6¦1 1„21†9 1…31‡01…7 1ƒ91†81„01‡21„2 1„01‡01„41ƒ91„5 1‚7 @$getMe->username 12 ”9ç9
6¦1 1„01‡21ƒ91…11…51„1 1‚7 @username 12"
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
        'text'=>"6¦1 1„21†9 1…31‡01…7 1ƒ91†81„01‡21„2 1„01‡01„41ƒ91„5 1‚7 @$getMe->username 12 ”9ç9
6¦1 1„01‡21ƒ91…11…51„1 1‚7 @username 12"
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
        'text'=>"6¦1 1„21†9 1…31‡01…7 1ƒ91†81„01‡21„2 1„01‡01„41ƒ91„5 1‚7 @$getMe->username 12 ”9ç9
6¦1 1„01‡21ƒ91…11…51„1 1‚7 @username 12"
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
        'text'=>"6¦1 1„21†9 1…31‡01…7 1ƒ91†81„01‡21„2 1„01‡01„41ƒ91„5 1‚7 @$getMe->username 12 ”9ç9
6¦1 1„01‡21ƒ91…11…51„1 1‚7 @username 12"
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
        'text'=>"6¦1 1„21†9 1…31‡01…7 1ƒ91†81„01‡21„2 1„01‡01„41ƒ91„5 1‚7 @$getMe->username 12 ”9ç9
6¦1 1„01‡21ƒ91…11…51„1 1‚7 @username 12"
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
        'text'=>"6¦1 1„21†9 1…31‡01…7 1ƒ91†81„01‡21„2 1„01‡01„41ƒ91„5 1‚7 @$getMe->username 12 ”9ç9
6¦1 1„01‡21ƒ91…11…51„1 1‚7 @username 12"
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
        'text'=>"6¦1 1„21†9 1…31‡01…7 1ƒ91†81„01‡21„2 1„01‡01„41ƒ91„5 1‚7 @$getMe->username 12 ”9ç9
6¦1 1„01‡21ƒ91…11…51„1 1‚7 @username 12"
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
        'text'=>"6¦1 1„21†9 1…31‡01…7 1ƒ91†81„01‡21„2 1„01‡01„41ƒ91„5 1‚7 @$getMe->username 12 ”9ç9
6¦1 1„01‡21ƒ91…11…51„1 1‚7 @username 12"
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
        'text'=>"6¦1 1„21†9 1…31‡01…7 1ƒ91†81„01‡21„2 1„01‡01„41ƒ91„5 1‚7 @$getMe->username 12 ”9ç9
6¦1 1„01‡21ƒ91…11…51„1 1‚7 @username 12"
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
        'text'=>"6¦1 1„21†9 1…31‡01…7 1ƒ91†81„01‡21„2 1„01‡01„41ƒ91„5 1‚7 @$getMe->username 12 ”9ç9
6¦1 1„01‡21ƒ91…11…51„1 1‚7 @username 12"
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
        'text'=>"6¦1 1„21†9 1…31‡01…7 1ƒ91†81„01‡21„2 1„01‡01„41ƒ91„5 1‚7 @$getMe->username 12 ”9ç9
6¦1 1„01‡21ƒ91…11…51„1 1‚7 @username 12"
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
        'text'=>"6¦1 1„21†9 1…31‡01…7 1ƒ91†81„01‡21„2 1„01‡01„41ƒ91„5 1‚7 @$getMe->username 12 ”9ç9
6¦1 1„01‡21ƒ91…11…51„1 1‚7 @username 12"
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
        'text'=>"6¦1 1„21†9 1…31‡01…7 1ƒ91†81„01‡21„2 1„01‡01„41ƒ91„5 1‚7 @$getMe->username 12 ”9ç9
6¦1 1„01‡21ƒ91…11…51„1 1‚7 @username 12"
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
        'text'=>"6¦1 1„21†9 1…31‡01…7 1ƒ91†81„01‡21„2 1„01‡01„41ƒ91„5 1‚7 @$getMe->username 12 ”9ç9
6¦1 1„01‡21ƒ91…11…51„1 1‚7 @username 12"
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
        'text'=>"6¦1 1„21†9 1…31‡01…7 1ƒ91†81„01‡21„2 1„01‡01„41ƒ91„5 1‚7 @$getMe->username 12 ”9ç9
6¦1 1„01‡21ƒ91…11…51„1 1‚7 @username 12"
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
        'text'=>"6¦1 1„21†9 1…31‡01…7 1ƒ91†81„01‡21„2 1„01‡01„41ƒ91„5 1‚7 @$getMe->username 12 ”9ç9
6¦1 1„01‡21ƒ91…11…51„1 1‚7 @username 12"
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
        'text'=>"6¦1 1„21†9 1…31‡01…7 1ƒ91†81„01‡21„2 1„01‡01„41ƒ91„5 1‚7 @$getMe->username 12 ”9ç9
6¦1 1„01‡21ƒ91…11…51„1 1‚7 @username 12"
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
        'text'=>"6¦1 1„21†9 1…31‡01…7 1ƒ91†81„01‡21„2 1„01‡01„41ƒ91„5 1‚7 @$getMe->username 12 ”9ç9
6¦1 1„01‡21ƒ91…11…51„1 1‚7 @username 12"
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
        'text'=>"6¦1 1„21†9 1…31‡01…7 1ƒ91†81„01‡21„2 1„01‡01„41ƒ91„5 1‚7 @$getMe->username 12 ”9ç9
6¦1 1„01‡21ƒ91…11…51„1 1‚7 @username 12"
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
        'text'=>"6¦1 1„21†9 1…31‡01…7 1ƒ91†81„01‡21„2 1„01‡01„41ƒ91„5 1‚7 @$getMe->username 12 ”9ç9
6¦1 1„01‡21ƒ91…11…51„1 1‚7 @username 12"
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
        'text'=>"6¦1 1„21†9 1…31‡01…7 1ƒ91†81„01‡21„2 1„01‡01„41ƒ91„5 1‚7 @$getMe->username 12 ”9ç9
6¦1 1„01‡21ƒ91…11…51„1 1‚7 @username 12"
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
        'text'=>"6¦1 1„21†9 1…31‡01…7 1ƒ91†81„01‡21„2 1„01‡01„41ƒ91„5 1‚7 @$getMe->username 12 ”9ç9
6¦1 1„01‡21ƒ91…11…51„1 1‚7 @username 12"
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
        'text'=>"6¦1 1„21†9 1…31‡01…7 1ƒ91†81„01‡21„2 1„01‡01„41ƒ91„5 1‚7 @$getMe->username 12 ”9ç9
6¦1 1„01‡21ƒ91…11…51„1 1‚7 @username 12"
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
        'text'=>"6¦1 1„21†9 1…31‡01…7 1ƒ91†81„01‡21„2 1„01‡01„41ƒ91„5 1‚7 @$getMe->username 12 ”9ç9
6¦1 1„01‡21ƒ91…11…51„1 1‚7 @username 12"
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
        'text'=>"6¦1 1„21†9 1…31‡01…7 1ƒ91†81„01‡21„2 1„01‡01„41ƒ91„5 1‚7 @$getMe->username 12 ”9ç9
6¦1 1„01‡21ƒ91…11…51„1 1‚7 @username 12"
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
        'text'=>"6¦1 1„21†9 1…31‡01…7 1ƒ91†81„01‡21„2 1„01‡01„41ƒ91„5 1‚7 @$getMe->username 12 ”9ç9
6¦1 1„01‡21ƒ91…11…51„1 1‚7 @username 12"
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
        'text'=>"6¦1 1„21†9 1…31‡01…7 1ƒ91†81„01‡21„2 1„01‡01„41ƒ91„5 1‚7 @$getMe->username 12 ”9ç9
6¦1 1„01‡21ƒ91…11…51„1 1‚7 @username 12"
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
        'text'=>"6¦1 1„21†9 1…31‡01…7 1ƒ91†81„01‡21„2 1„01‡01„41ƒ91„5 1‚7 @$getMe->username 12 ”9ç9
6¦1 1„01‡21ƒ91…11…51„1 1‚7 @username 12"
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
        'text'=>"6¦1 1„21†9 1…31‡01…7 1ƒ91†81„01‡21„2 1„01‡01„41ƒ91„5 1‚7 @$getMe->username 12 ”9ç9
6¦1 1„01‡21ƒ91…11…51„1 1‚7 @username 12"
    ]);
    $webhook = file_get_contents("https://api.telegram.org/bot".file_get_contents("make.txt")."/setwebhook?url=".$_SERVER['SERVER_NAME'].'/bots/'.file_get_contents("make.txt").'/bot29.php');
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>$webhook
    ]);
    unlink("make.txt");
    unlink("mode.txt");
}t_id'=>$chat_id2,
        'text'=>"â€„1¤7 ØªÙ… ØµÙ†Ø¹ Ø§Ù„Ø¨ÙˆØª Ø¨Ù†Ø¬Ø§Ø­ Ø› @$getMe->username ØŒ ðŸ”±
â€„1¤7 Ø¨ÙˆØ§Ø³Ø·Ø© Ø› @username ØŒ"
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
        'text'=>"â€„1¤7 ØªÙ… ØµÙ†Ø¹ Ø§Ù„Ø¨ÙˆØª Ø¨Ù†Ø¬Ø§Ø­ Ø› @$getMe->username ØŒ ðŸ”±
â€„1¤7 Ø¨ÙˆØ§Ø³Ø·Ø© Ø› @username ØŒ"
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
        'text'=>"â€„1¤7 ØªÙ… ØµÙ†Ø¹ Ø§Ù„Ø¨ÙˆØª Ø¨Ù†Ø¬Ø§Ø­ Ø› @$getMe->username ØŒ ðŸ”±
â€„1¤7 Ø¨ÙˆØ§Ø³Ø·Ø© Ø› @username ØŒ"
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
        'text'=>"â€„1¤7 ØªÙ… ØµÙ†Ø¹ Ø§Ù„Ø¨ÙˆØª Ø¨Ù†Ø¬Ø§Ø­ Ø› @$getMe->username ØŒ ðŸ”±
â€„1¤7 Ø¨ÙˆØ§Ø³Ø·Ø© Ø› @username ØŒ"
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
        'text'=>"â€„1¤7 ØªÙ… ØµÙ†Ø¹ Ø§Ù„Ø¨ÙˆØª Ø¨Ù†Ø¬Ø§Ø­ Ø› @$getMe->username ØŒ ðŸ”±
â€„1¤7 Ø¨ÙˆØ§Ø³Ø·Ø© Ø› @username ØŒ"
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
        'text'=>"â€„1¤7 ØªÙ… ØµÙ†Ø¹ Ø§Ù„Ø¨ÙˆØª Ø¨Ù†Ø¬Ø§Ø­ Ø› @$getMe->username ØŒ ðŸ”±
â€„1¤7 Ø¨ÙˆØ§Ø³Ø·Ø© Ø› @username ØŒ"
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
        'text'=>"â€„1¤7 ØªÙ… ØµÙ†Ø¹ Ø§Ù„Ø¨ÙˆØª Ø¨Ù†Ø¬Ø§Ø­ Ø› @$getMe->username ØŒ ðŸ”±
â€„1¤7 Ø¨ÙˆØ§Ø³Ø·Ø© Ø› @username ØŒ"
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
        'text'=>"â€„1¤7 ØªÙ… ØµÙ†Ø¹ Ø§Ù„Ø¨ÙˆØª Ø¨Ù†Ø¬Ø§Ø­ Ø› @$getMe->username ØŒ ðŸ”±
â€„1¤7 Ø¨ÙˆØ§Ø³Ø·Ø© Ø› @username ØŒ"
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
        'text'=>"â€„1¤7 ØªÙ… ØµÙ†Ø¹ Ø§Ù„Ø¨ÙˆØª Ø¨Ù†Ø¬Ø§Ø­ Ø› @$getMe->username ØŒ ðŸ”±
â€„1¤7 Ø¨ÙˆØ§Ø³Ø·Ø© Ø› @username ØŒ"
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
        'text'=>"â€„1¤7 ØªÙ… ØµÙ†Ø¹ Ø§Ù„Ø¨ÙˆØª Ø¨Ù†Ø¬Ø§Ø­ Ø› @$getMe->username ØŒ ðŸ”±
â€„1¤7 Ø¨ÙˆØ§Ø³Ø·Ø© Ø› @username ØŒ"
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
        'text'=>"â€„1¤7 ØªÙ… ØµÙ†Ø¹ Ø§Ù„Ø¨ÙˆØª Ø¨Ù†Ø¬Ø§Ø­ Ø› @$getMe->username ØŒ ðŸ”±
â€„1¤7 Ø¨ÙˆØ§Ø³Ø·Ø© Ø› @username ØŒ"
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
        'text'=>"â€„1¤7 ØªÙ… ØµÙ†Ø¹ Ø§Ù„Ø¨ÙˆØª Ø¨Ù†Ø¬Ø§Ø­ Ø› @$getMe->username ØŒ ðŸ”±
â€„1¤7 Ø¨ÙˆØ§Ø³Ø·Ø© Ø› @username ØŒ"
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
        'text'=>"â€„1¤7 ØªÙ… ØµÙ†Ø¹ Ø§Ù„Ø¨ÙˆØª Ø¨Ù†Ø¬Ø§Ø­ Ø› @$getMe->username ØŒ ðŸ”±
â€„1¤7 Ø¨ÙˆØ§Ø³Ø·Ø© Ø› @username ØŒ"
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
        'text'=>"â€„1¤7 ØªÙ… ØµÙ†Ø¹ Ø§Ù„Ø¨ÙˆØª Ø¨Ù†Ø¬Ø§Ø­ Ø› @$getMe->username ØŒ ðŸ”±
â€„1¤7 Ø¨ÙˆØ§Ø³Ø·Ø© Ø› @username ØŒ"
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
        'text'=>"â€„1¤7 ØªÙ… ØµÙ†Ø¹ Ø§Ù„Ø¨ÙˆØª Ø¨Ù†Ø¬Ø§Ø­ Ø› @$getMe->username ØŒ ðŸ”±
â€„1¤7 Ø¨ÙˆØ§Ø³Ø·Ø© Ø› @username ØŒ"
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
        'text'=>"â€„1¤7 ØªÙ… ØµÙ†Ø¹ Ø§Ù„Ø¨ÙˆØª Ø¨Ù†Ø¬Ø§Ø­ Ø› @$getMe->username ØŒ ðŸ”±
â€„1¤7 Ø¨ÙˆØ§Ø³Ø·Ø© Ø› @username ØŒ"
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
        'text'=>"â€„1¤7 ØªÙ… ØµÙ†Ø¹ Ø§Ù„Ø¨ÙˆØª Ø¨Ù†Ø¬Ø§Ø­ Ø› @$getMe->username ØŒ ðŸ”±
â€„1¤7 Ø¨ÙˆØ§Ø³Ø·Ø© Ø› @username ØŒ"
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
        'text'=>"â€„1¤7 ØªÙ… ØµÙ†Ø¹ Ø§Ù„Ø¨ÙˆØª Ø¨Ù†Ø¬Ø§Ø­ Ø› @$getMe->username ØŒ ðŸ”±
â€„1¤7 Ø¨ÙˆØ§Ø³Ø·Ø© Ø› @username ØŒ"
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
        'text'=>"â€„1¤7 ØªÙ… ØµÙ†Ø¹ Ø§Ù„Ø¨ÙˆØª Ø¨Ù†Ø¬Ø§Ø­ Ø› @$getMe->username ØŒ ðŸ”±
â€„1¤7 Ø¨ÙˆØ§Ø³Ø·Ø© Ø› @username ØŒ"
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
        'text'=>"â€„1¤7 ØªÙ… ØµÙ†Ø¹ Ø§Ù„Ø¨ÙˆØª Ø¨Ù†Ø¬Ø§Ø­ Ø› @$getMe->username ØŒ ðŸ”±
â€„1¤7 Ø¨ÙˆØ§Ø³Ø·Ø© Ø› @username ØŒ"
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
        'text'=>"â€„1¤7 ØªÙ… ØµÙ†Ø¹ Ø§Ù„Ø¨ÙˆØª Ø¨Ù†Ø¬Ø§Ø­ Ø› @$getMe->username ØŒ ðŸ”±
â€„1¤7 Ø¨ÙˆØ§Ø³Ø·Ø© Ø› @username ØŒ"
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
        'text'=>"â€„1¤7 ØªÙ… ØµÙ†Ø¹ Ø§Ù„Ø¨ÙˆØª Ø¨Ù†Ø¬Ø§Ø­ Ø› @$getMe->username ØŒ ðŸ”±
â€„1¤7 Ø¨ÙˆØ§Ø³Ø·Ø© Ø› @username ØŒ"
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
        'text'=>"â€„1¤7 ØªÙ… ØµÙ†Ø¹ Ø§Ù„Ø¨ÙˆØª Ø¨Ù†Ø¬Ø§Ø­ Ø› @$getMe->username ØŒ ðŸ”±
â€„1¤7 Ø¨ÙˆØ§Ø³Ø·Ø© Ø› @username ØŒ"
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
        'text'=>"â€„1¤7 ØªÙ… ØµÙ†Ø¹ Ø§Ù„Ø¨ÙˆØª Ø¨Ù†Ø¬Ø§Ø­ Ø› @$getMe->username ØŒ ðŸ”±
â€„1¤7 Ø¨ÙˆØ§Ø³Ø·Ø© Ø› @username ØŒ"
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
        'text'=>"â€„1¤7 ØªÙ… ØµÙ†Ø¹ Ø§Ù„Ø¨ÙˆØª Ø¨Ù†Ø¬Ø§Ø­ Ø› @$getMe->username ØŒ ðŸ”±
â€„1¤7 Ø¨ÙˆØ§Ø³Ø·Ø© Ø› @username ØŒ"
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
        'text'=>"â€„1¤7 ØªÙ… ØµÙ†Ø¹ Ø§Ù„Ø¨ÙˆØª Ø¨Ù†Ø¬Ø§Ø­ Ø› @$getMe->username ØŒ ðŸ”±
â€„1¤7 Ø¨ÙˆØ§Ø³Ø·Ø© Ø› @username ØŒ"
    ]);
    $webhook = file_get_contents("https://api.telegram.org/bot".file_get_contents("make.txt")."/setwebhook?url=".$_SERVER['SERVER_NAME'].'/bots/'.file_get_contents("make.txt").'/bot29.php');
    bot('sendmessage',[
        'chat_id'=>$chat_id2,
        'text'=>$webhook
    ]);
    unlink("make.txt");
    unlink("mode.txt");
}
