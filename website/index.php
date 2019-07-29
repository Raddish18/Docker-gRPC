<html>
	<head> 
		<title>Logs</title>
	<head>
	
	<body>
		<h1>Logs</h1>
		<h2>Alerts:</h2>
		<ul>
			<?php
				$json = file_get_contents('http://product-service');
				$obj = json_decode($json);

				ob_implicit_flush(true);
				ob_end_flush();
				$products = $obj->products;
				foreach($products as $product){
					echo"<li>$product</li>";
					sleep(3);
				}
			?>
		</ul>
	</body>
</html>
