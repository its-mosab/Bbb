const TelegramBot = require('node-telegram-bot-api');
const token = '7225739052:AAF0e4cNK9WM0EZI7YnzK_S5t0tvLIOtMsQ';
const bot = new TelegramBot(token, { polling: true });

bot.onText(/\/start/, (msg) => {
    const chatId = msg.chat.id;
    const opts = {
        reply_markup: {
            inline_keyboard: [
                [
                    {
                        text: 'افتح التطبيق',
                        web_app: { url: 'https://its-mosab.github.io/Bbb/index.html' }
                    }
                ]
            ]
        }
    };
    bot.sendMessage(chatId, 'اضغط على الزر لفتح التطبيق:', opts);
});
