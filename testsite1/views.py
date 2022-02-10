from django.http import HttpResponse

helloWorld = """
<!DOCTYPE html>
<html>
<head>
<title>Hello world!</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Yellowtail&display=swap" rel="stylesheet">
<style>
  h1 {
      font-family: 'Yellowtail', cursive;
  }

  img {
      width: 50vw;
  }
</style>
</head>
<body>
  <div>
    <h1>Hello world!</h1>
    <img src="https://i.imgur.com/GCSyp4A.png" />
  </div>
</body>
</html>
"""


def index(request):
    return HttpResponse(helloWorld)
