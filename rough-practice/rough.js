function printRandomMotivationalQuote() {
    const quotes = [
        "The best way to get started is to quit talking and begin doing. - Walt Disney",
        "The pessimist sees difficulty in every opportunity. The optimist sees opportunity in every difficulty. - Winston Churchill",
        "Don’t let yesterday take up too much of today. - Will Rogers",
        "You learn more from failure than from success. Don’t let it stop you. Failure builds character. - Unknown",
        "It’s not whether you get knocked down, it’s whether you get up. - Vince Lombardi",
        "If you are working on something that you really care about, you don’t have to be pushed. The vision pulls you. - Steve Jobs",
        "People who are crazy enough to think they can change the world, are the ones who do. - Rob Siltanen",
        "Failure will never overtake me if my determination to succeed is strong enough. - Og Mandino",
        "Entrepreneurs are great at dealing with uncertainty and also very good at minimizing risk. That’s the classic entrepreneur. - Mohnish Pabrai",
        "We may encounter many defeats but we must not be defeated. - Maya Angelou",
        "You miss 100 percent of the shots you don’t take. - Wayne Gretzky",
        "I have not failed. I’ve just found 10,000 ways that won’t work. - Thomas Edison",
        "You are never too old to set another goal or to dream a new dream. - C.S. Lewis",
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Keep your eyes on the stars, and your feet on the ground. - Theodore Roosevelt",
        "I am not a product of my circumstances. I am a product of my choices. - Unknown",
        "The best revenge is massive success. - Frank Sinatra",
        "Believe you can and you are halfway there. - Theodore Roosevelt",
        "It is our choices, Harry, that show what we truly are, far more than our abilities. - J.K. Rowling"
    ];
    let size = quotes.length
    const randomIndex = Math.floor( Math.random() * size) 

    quotes.forEach((obj , index) => {
        console.log(index)
        console.log(`hello --- ${obj} ----- hello` )
    })
}

// Run the function to print a random motivational quote
printRandomMotivationalQuote();