using System;
using WebSocketSharp;

namespace cs_client
{
    class Program
    {
        static void Main(string[] args)
        {
            using ( WebSocket ws = new WebSocket("ws://127.0.0.1:5000"))
            { 
           
                ws.Connect();
                ws.Send("hi serv");
             

                ws.OnMessage += Ws_OnMessage;

                Console.ReadKey();
            };
        }

        private static void Ws_OnMessage(object sender, MessageEventArgs e)
        {
            Console.WriteLine("Received from server " + e.Data);
        }
    }
}
