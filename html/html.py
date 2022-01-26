TOPHTML = '''<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">    
    <link rel="stylesheet" href="../html/ac.css">
    <link type="image/x-icon" rel="shortcut icon" href="favicon.ico">
    <title>LinePoets works</title>
</head>
<body>    

    <h1>LinePoets works</h1>

    <table>
        <tr>
            <th><div>№</div></th>
            <th><div>Thumbnail</div></th>
            <th><div>Name</div></th>
            <th><div>Date</div></th>
            <th><div>Full path</div></th>
        </tr>

'''

CONTENTHTML = '''
        <tr{}>
            <td><div>{}</div></td>
            <td>
                <div class="jpg">
                    <img src="img/{}.jpg" alt="">
                </div>
            </td>
            <td><div>{}</div></td>
            <td><div>{}</div></td>
            <td><div>{}</div></td>
        </tr>
'''

BOTTOMHTML = '''
    </table>

</body>
</html>
'''
