
client = new Paho.Client("95.188.85.203", Number(9001), "/ws", "clientId11");

client.onConnectionLost = function (responseObject) {
    console.log("Connection Lost: "+responseObject.errorMessage);
    inactive_connect_to_mqtt
}

client.onMessageArrived = function (message) {
  console.log("Message Arrived: "+message.payloadString);
  mqtt_string = message.payloadString
  replca_val(mqtt_string)
}

// Called when the connection is made
function onConnect(){
    console.log('on connect');
    var start_topic = 'holod/';
    var imei_str = imei;
    var topic = start_topic + imei_str;
    // var topic = topic_for_sub
    console.log(topic)
    client.subscribe(topic);
    active_connect_to_mqtt();
}

// Connect the client, providing an onConnect callback
client.connect({
    onSuccess: onConnect,
    onFailure: inactive_connect_to_mqtt,
    userName : 'site',
    password : 'site'
});


function onConnectionLost(responseObject) {
  if (responseObject.errorCode !== 0)
	console.log("onConnectionLost:"+responseObject.errorMessage);
};


function replca_val(mqtt_string) {
    try{
        mqtt_string = JSON.parse(mqtt_string)
    }
    catch {
        console.log('Error parce mqtt string')
    }

    finally {
        for (let key in mqtt_string){
        let element_ = key;
        element_ = 'online'+'_'+key;
        console.log(element_);
        let block = document.getElementById(element_);
        if (block !== null){
            // console.log('БЛОК найдет');
            block.innerHTML = mqtt_string[key];
        }
        else {
            console.log(' Блок не найден');
        }
    }
    let block = document.getElementById('online_date');
    block.innerHTML = new Date()

    console.log(block)
    }
    
    // console.log(mqtt_string)


}

function active_connect_to_mqtt(){
    let block = document.getElementById("indicator");
        if (block !== null){
            // console.log(block);
            block.className="indicator-status"
        }
        else {
            console.log('Блок индикатор не найден');
        }
}

function inactive_connect_to_mqtt(){
    let block = document.getElementById("indicator");
        if (block !== null){
            // console.log(block);
            block.className="indicator-status-offline"
        }
        else {
            console.log('Блок индикатор не найден');
        }
}

function conect_lost(){
    console.log('Lost');
}

