

const url= 'https://favqs.com/api/quotes'


let quoteOftheDay = document.getElementById('quote')


let authorQuote = document.querySelector('#author')


axios.get(url, {
    headers: {
        'Authorization': `Token token="${API_Key}"`
    }
})

  .then(function (response) {
    // handle success
    
    data = response.data.quotes   //25quote info
    data.forEach( quote => {
        let q_body = document.createElement("div")
        let body_text = quote.body;
        q_body.innerText= body_text;
        q_body.setAttribute('class', 'quote_body')
        
        let author = document.createElement("p")
        let author_text = quote.author;
        author.innerText= author_text;
        author.setAttribute('id', 'author_dash')
        document.body.appendChild(q_body)
        document.body.appendChild(author)

        console.log(quote) 

    
  })
  .catch(function (error) {
    // handle error
    console.log(error);
  })
  .finally(function () {
    // always executed
  });

 