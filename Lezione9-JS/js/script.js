// Questo è un commento in JS
    /* anche questo è un commeto in JS, solo che questo è multilinea
    e può essere lungo quanto vogliamo */



    // Dichiaro una variabile utilizzando la parola chiave let
    let mioNome = "Mario"; //stringa
    let mioCognome = "Rossi"; //stringa

    let miaEtà = 30; //number


    //chiedo di che tipo è la variabile

    console.log(typeof(mioNome)); //stringa
    console.log(typeof(mioCognome)); //stringa

    //Per poter vedere lo script e la relativa console devo usare il browser
    console.log("Ciao " + mioNome + " " + mioCognome + ", hai " + miaEtà + " anni"); //stringa

//dimostro come Javascript sia un linguaggio DEBOLMENTE TIPIZZATO



    let numero1 = "10"; //erroneamente verrebbe 108.5


    //Tutte le altre sono operazioni tipo matematico quindi non fa altro che svolgerle come sempre

    let numero2 = 8.5; //number

   // let somma = numero1 + numero2; //number
   //posso anche in questo caso, fare il cast del dato
   
   let somma = Number(numero1) + numero2; //number


   let sottrazione = numero1 - numero2; //number
    let moltiplicazione = numero1 * numero2; //number
    let divisione = numero1 / numero2; //number

    console.log(somma);
    console.log(sottrazione);
    console.log(moltiplicazione);
    console.log(divisione);


    //COSTRUTTI - PARADIGMA FONDAMENTALE della
    if(miaEtà >= 18){
        console.log("Benvenuto");
    }else{
        console.log("Non puoi entrare");
    }

    for(let i = 0; i < 10; i++){
        console.log(i);
    }