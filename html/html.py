TOPHTML = '''<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">    
    <link rel="stylesheet" href="../html/ac.css">
    <title>Document</title>
</head>
<body>    

    <table>
        <tr>
            <th>№</th>
            <th>Thumbnail</th>
            <th>Name</th>
            <th>Date</th>
        </tr>

'''

CONTENTHTML = '''
        <tr{}>
            <td>{}</td>
            <td>
                <div class="jpg">
                    <img src="img/{}.jpg" alt="">
                </div>
            </td>
            <td>{}</td>
            <td>{}</td>
        </tr>
'''

BOTTOMHTML = '''
    </table>

</body>
</html>
'''
