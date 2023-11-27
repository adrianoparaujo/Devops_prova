from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/historia')
def historia():
    return '''
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Max Solaris</title>
    <link rel="stylesheet" href="style.css">
     
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
