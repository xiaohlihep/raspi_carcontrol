    <html>
    <head>
    <title>Car Control</title>
    <link rel="stylesheet" href="../css/bootstrap.min.css">
  <script src="../js/jquery.min.js"></script>
  <script src="../js/bootstrap.min.js"></script>
    </head>
    <body>
    <div class="container-fluid">
    <br>
    <br>
    <br>
    <br>
    <br>
  <div class="row">
	  <div class="col-sm-4"></div>
	  <div class="col-sm-4"><button href="index.py?M=F&T=1&P=0.5" class="btn-lg btn-info" role="button">  |   Go    |</button></div>
	  <div class="col-sm-4"></div>
  </div>
  <br>
  <div class="row">
	  <div class="col-sm-2"></div>
	  <div class="col-sm-4"><button href="index.py?M=L&T=0.3&P=0.4" class="btn-lg btn-info" role="button">Left</button></div>
	  <div class="col-sm-4"><button href="index.py?M=R&T=0.3&P=0.4" class="btn-lg btn-info" role="button">Right</button> </div>
	  <div class="col-sm-2"></div>
  </div>
  <br>
  <div class="row">
	  <div class="col-sm-4"></div>
	  <div class="col-sm-4"><button href="index.py?M=B&T=1&P=0.5" class="btn-lg btn-info" role="button">Back</button></div>
	  <div class="col-sm-4"></div>
  </div>
  <br>
  <br>
  <h3>Taking photo</h3>
  <button id="takephoto" type="button" class="btn btn-success">Start </button>
  <button id="stoptakingphoto" type="button" class="btn btn-success">Stop </button>
  <br>
  <div id="msg"> </div>
  <br>
  <div class="row">
	  <div class="col-sm-12">
          <img id="photo" src="../cam.jpg" width="600px"></div>
  </div>
  <br>
  
  <br>
  <br>
  <br>

<div class="form-group">
<form action="index.py" method="Get">
  <input class="form-control" type="text" name="M" value="F"><br>
  <input class="form-control" type="text" name="T" value="1"><br>
  <input class="form-control" type="text" name="P" value="0.5"><br>
  <input class="form-control" type="submit" value="Go">
</form>
</div>


</div>
</body>
</html>
