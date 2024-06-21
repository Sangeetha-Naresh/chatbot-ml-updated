$(document).ready(function () 
{
  
})

function displayBot() 
{
    // Binds a click event to the .chatbox__button element, 
    // toggling the visibility of .chatbox__chat when clicked.
    

    //Start Conversation with Bot
    
}

function askBot() 
{
    $("").click(function () {
        
     
        var user_bot_input_text = $("").val()

        if (user_bot_input_text != "") 
        {
           
        
            $("#chat_messages").append('<div class="user__messages">' +  + ' </div>')
            
            //Clear the text input box after sending message
            $("").val('');

          
            let chat_input_data = 
            {
               
            }
            
            
            $.ajax({
                
                type: 'POST',

                url: "",

                
                data:JSON.stringify(yourData) ,

                
                dataType: "json",

                contentType: 'application/json',

               
                    success: function (result) 
                    {
                        //  Appends the bot's response (contained in result.bot_response) to the chat messages container.
                                         
                        
                       //  Scroll the chat messages container to the bottom over a duration of 1 second (1000 milliseconds),
                      
                        }    ,

                    // A callback function that is executed if the request fails.
                    error: function (result) {
                        alert(result.responseJSON.message)
                    }
            });

        }

    })

    
    $('#bot_input_text').keypress(function(e)
    {
        //If Enter key(key code is 13) pressed
        
        {         
             //Trigger Send Button Click Event

        }
    });
}
