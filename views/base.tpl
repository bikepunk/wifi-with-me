<!DOCTYPE html>
<html lang="fr">
  <head>
    <meta charset="utf-8">
    <title>Réseau radio de tetaneutral.net</title>

    <!-- jQuery -->
    <script src="assets/jquery/jquery-1.11.0.min.js" type="text/javascript"></script>

    <!-- Bootstrap -->
    <script src="assets/bootstrap/js/bootstrap.js"></script>
    <link href="assets/bootstrap/css/bootstrap.min.css" rel="stylesheet">

    <!-- Leaflet -->
    <link rel="stylesheet" type="text/css" media="all" href="assets/leaflet/leaflet.css" />
    <script src="assets/leaflet/leaflet.js" type="text/javascript"></script>
    <!-- Leaflet-semicircle -->
    <script src="assets/leaflet-semicircle/semicircle.js" type="text/javascript"></script>

    <!-- Custom -->
    <link rel="stylesheet" type="text/css" media="all" href="assets/main.css" />


  </head>
<body class="{{page}}">

  <header class="main-header jumbotron">
    <div class="container">
    %if page == 'form':
    <h1>Réseau radio de tetaneutral.net</h1>
    %else:
    <h1><a href="./">Réseau radio de tetaneutral.net</a></h1>
    %end
    </div>
  </header>

  <section role="main" class="container">
  %include
  </section>

  <footer>
    <p>
        Les données personnelles que vous ne rendez pas publiques
	sont stockées exclusivement chez tetaneutral.net durant un an (sauf demande de votre part)
	et ne seront pas partagées avec d'autres
	associations, entreprises ou collectivités. Des membres de
	tetaneutral.net seront toutefois amenés à les étudier : ne
	fournissez pas de données si vous n'avez pas confiance en tetaneutral.net.
        <br>
        <a href="//tetaneutral.net" target="_blank">tetaneutral.net</a> -
        <a href="./legal">Vos droits d'accès et de rectification de vos données
	personnelles</a>
    </p>
  </footer>

</body>
</html>
