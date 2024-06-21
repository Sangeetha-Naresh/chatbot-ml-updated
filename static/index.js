//Ensures that the DOM is fully loaded before executing any JavaScript code.
$(document).ready(function () 
{
  displayBot()
})

function displayBot() {
    // Binds a click event to the .chatbox__button element, 
    // toggling the visibility of .chatbox__chat when clicked.
    $('.chatbox__button').click(function () {
     // jQuery selector used to select HTML elements with the class chatbox__button.
        // When the chatbox_button is clicked, the chatbox_chat div will pop up 
        //using the toggle() function
        
        $('.chatbox__chat').toggle()
    });
    //Start Conversation with Bot
    askBot()
}

function askBot() {
    $("#send_button").click(function () {
        //This is a jQuery selector that selects the HTML element with the ID send_button.
        var user_bot_input_text = $("#bot_input_text").val()

        if (user_bot_input_text != "") {
           
            $("#chat_messages").append('<div class="user__messages">' + user_bot_input_text + ' </div>')
            
            //Clear the text input box after sending message
            $("#bot_input_text").val('');

            //is creating a JavaScript object named chat_input_data with a single property. 
            let chat_input_data = {
                "user_bot_input_text": user_bot_input_text
            }
            
            // Asynchronous JavaScript and XML -AJAX
            //The code snippet provided is an AJAX request using jQuery's $.ajax() method. 
            //This request is configured to send data to a server endpoint and handle the response.
            
            // The $.ajax() function is used to perform asynchronous HTTP (Ajax) requests.
            $.ajax({
                //Specifies the type of request to be made, in this case, a POST request.
                type: 'POST',

                //The URL to which the request is sent. In this case, it is /bot-response.
                url: "/bot-response",

                // The data to be sent to the server. 
                //chat_input_data is converted to a JSON string using JSON.stringify()
                data: JSON.stringify(chat_input_data),

                //The type of data expected back from the server. 
                //In this case, the server's response is expected to be in JSON format.
                dataType: "json",

                //The content type of the data being sent to the server.
                // It specifies that the request payload is in JSON format.
                contentType: 'application/json',

                //A callback function that is executed if the request succeeds. 
                //The result parameter contains the data returned from the server.
                success: function (result) {
                        //  Appends the bot's response (contained in result.bot_response) to the chat messages container.
                        $("#chat_messages").append('<div class="bot__messages">' + result.bot_response + ' </div>')                        
                        
                        //  Scrolls the chat messages container to the bottom over a duration of 1 second (1000 milliseconds),
                        // ensuring the latest message is visible. 
                        $('.chatbox__messages__cotainer').animate({
                            scrollTop: $('.chatbox__messages__cotainer')[0].scrollHeight}, 1000);
                },

                    // A callback function that is executed if the request fails.
                error: function (result) {
                        alert(result.responseJSON.message)
                }
            });

        }

    })


    $('#bot_input_text').keypress(function(e){
        //If Enter key(key code is 13) pressed
        if(e.which == 13){         
            $('#send_button').click(); //Trigger Send Button Click Event
        }
    });
}
