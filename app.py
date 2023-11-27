from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return '''
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Max Solaris</title>
    <link rel="stylesheet" href="style.css">
      <style> *{
    padding: 0;
    margin: 0;
}
.fundo{
    background: url(img/bg2.jpg) no-repeat;
    background-size: 100% 100%;	
    background-position: center;
    height: 100vh;
	
}
.fundo-historia{
    background: url(img/bg-historia.jpg) no-repeat;
    background-size: 100% 100%;	
    background-position: center;
	height: 100vh;
}
.fundo-historia::before {
	content: "";
	background-color: rgba(13, 2, 2, 0.4);
	position: absolute;
	top: 0;
	left: 0;
	bottom: 0;
	right: 0;
}
.fundo-formacao{
    background: url(img/bg-formacao.jpg) no-repeat;
    background-size: 100% 100%;	
    background-position: center;
	height: 100vh;
}
.fundo-projetos{
    background: url(img/bg-projetos.jpg) no-repeat;
    background-size: 100% 100%;	
    background-position: center;
	height: 100vh;
}
.fundo-projetos::before {
	content: "";
	background-color: rgba(13, 2, 2, 0.4); 
	position: absolute;
	top: 0;
	left: 0;
	bottom: 0;
	right: 0;
}
.fundo-premios{
    background: url(img/bg-premios.jpg) no-repeat;
    background-size: 100% 100%;	
    background-position: center;
	height: 100vh;
}
.fundo-premios::before {
	content: "";
	background-color: rgba(13, 2, 2, 0.4);
	position: absolute;
	top: 0;
	left: 0;
	bottom: 0;
	right: 0;
}
.fundo-contato{
    background: url(img/bg-contato.jpg) no-repeat;
    background-size: 100% 100%;	
    background-position: center;
	height: 100vh;
}




.barranave{
    position: fixed;
    height: 80px;
    width: 100%;
    top: 0;
	left: 0;
    background:  rgba(0,0,0,0.4);
}
.barranave ul{
    float: right;
    margin-right: 20px;
}
.barranave ul li{
    list-style: none;
    margin: 0 8px;
    display: inline-block;
    line-height: 80px;
}
ul li a{
	font-size: 20px;
	font-family: 'Arial', sans-serif;
	color: white;
	padding: 6px 13px;
	text-decoration: none;
	transition: .4s;
}
.barranave ul li a.active,
.barranave ul li a:hover{
	background: red;
	border-radius: 2px;
}
.barranave .logo{
    width: 80px;
    height: auto;
    padding: 20px 100px;
}




.fundo .CentroTexto{
	position: fixed;
	left: 5%;
	top: 25%;
	font-family: sans-serif;
	user-select: none;
}

.CentroTexto h1{
	color: white;
	font-size: 70px;
	width: 900px;
	font-weight: bold;
	text-align: left;
}
.CentroTexto h2{
	color: rgb(255, 255, 255);
	font-size: 50px;
	font-weight: bold;
	margin-top: 10px;
	width: 885px;
	text-align: left;    
}

.fundo .resumo{
	position: fixed;
	left: 45%;
	top: 25%;
	font-family: sans-serif;
	user-select: none;
}
.resumo h1{
	color: white;
	font-size: 20px;
	width: 800px;
	font-weight: normal;
	text-align: left;
	
}
.resumo h2{
	color: white;
	font-size: 20px;
	width: 900px;
	font-weight: normal;
	text-align: left;
}
.resumo h3{
	color: white;
	font-size: 20px;
	width: 900px;
	font-weight: normal;
	text-align: left;
}

/* HISTORIA */

.fundo-historia .historia-Texto{
	position: fixed;
	left: 5%;
	top: 15%;
	font-family: sans-serif;
	user-select: none;
}
.historia-Texto h1{
	color: white;
	font-size: 50px;
	width: 900px;
	font-weight: bold;
	text-align: left;
}
.fundo-historia .resumo-historia{
	position: fixed;
	color: aliceblue;
	left: 5%;
	top: 30%;
	font-family: sans-serif;
	user-select: none;

}


/* FORMAÇÃO */


.fundo-formacao .resumo-formacao{
	position: fixed;
	color: aliceblue;
	left: 5%;
	top: 20%;
	font-family: sans-serif;
	user-select: none;
}


/* projetos */


.fundo-projetos .projetos-Texto{
	position: fixed;
	left: 5%;
	top: 15%;
	font-family: sans-serif;
	user-select: none;
}
.projetos-Texto h1{
	color: white;
	font-size: 50px;
	width: 900px;
	font-weight: bold;
	text-align: left;
}
.fundo-projetos .resumo-projetos{
	position: fixed;
	color: aliceblue;
	left: 5%;
	top: 30%;
	font-family: sans-serif;
	user-select: none;

}


/* premios */


.fundo-premios .resumo-premios{
	position: fixed;
	color: aliceblue;
	left: 5%;
	top: 20%;
	font-family: sans-serif;
	user-select: none;
}




/* formulário de contato */

.formulario-contato {
    width: 80%;
    max-width: 600px;
    margin: 0 auto;
    padding: 20px;
    background-color: rgba(255, 255, 255, 0.4); 
    border: 1px solid #ccc;
    border-radius: 5px;
    position: fixed; 
    top: 30%;
	left: 30%; 
    
}

.formulario-contato h2 {
    font-size: 24px;
    margin: 0 0 20px;
}

.formulario-contato label {
    display: block;
    margin-bottom: 5px;
}

.formulario-contato input[type="text"],
.formulario-contato input[type="email"],
.formulario-contato textarea {
    width: 100%;
    padding: 10px;
    margin-bottom: 15px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

.formulario-contato button {
    background-color: #0074e4;
    color: #fff;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

.formulario-contato button:hover {
    background-color: #005ea1;
}

</style>
</head>
<body>
    <div class="fundo">
        <nav class="barranave">
            <a href="index.html">  <img class="logo" src="img/logo.png" > </a>
            <ul>
                <li><a href="historia.html"> Historia </a> </li>
                <li><a href="formacao.html"> Formação </a> </li>    
                <li><a href="projetos.html"> Projetos </a> </li>
                <li><a href="premios.html"> Prêmios </a> </li>  
                <li><a href="Contato.html"> Contato </a> </li>                  
            </ul>
        </nav>
        <div class="CentroTexto">
            <h1> Max Solaris </h1>
            <h2> Aventureiro Espacial </h2>

        </div>

        <div class="resumo">
            <h1> Max Solaris é um renomado astronauta conhecido por suas incríveis habilidades.</h1><br/>
            <h2> Desde muito jovem demonstrou uma paixão ardente pelo cosmos.</h2><br/>
            <h3> Sua jornada rumo às estrelas começou com uma sólida formação educacional.</h3>  
             
        </div>

    </div> 
</body>
</html>


'''
