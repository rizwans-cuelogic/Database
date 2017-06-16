 function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

 app.controller('MainController',['$scope','$http',function($scope,$http) { 
  $scope.prds=[];
  $scope.title = 'JEWELLERY SHOP'; 
  $scope.promo = 'The most popular JEWELLERY this month.';
  $scope.products=[{ name: 'Azurite', price: 3.95 , desc: 'Some of Gems ARE PRECIOUS FOR ',
					canpurchase:true	
					},
				{ name: 'Pentagon', price: 66.95 , desc: 'lorem ipsum dgfdg gdfgfdg drgr rgerg ',
					canpurchase:true	
					},
				{ name: 'Dedrahydron', price:102.95 , desc: 'sdfh ioefe efir feerf fgreg ffr ',
					canpurchase:true	
					},
				{ name: 'Diamond', price: 2222.95 , desc: 'dsfsdjf siefi efe regej regj rge ',
					canpurchase:true	
					}			
				]
        
$http.get('/products/').then(function(response){
  		$scope.prds=response.data
})

}]);

app.controller('PanelController',function(){
	this.tab=1;
	this.selectTab = function(setTab){
		this.tab=setTab
	}
	this.isSelected = function( checkTab ){
		return this.tab === checkTab
	}
});
app.config(['$qProvider', function ($qProvider) {
    $qProvider.errorOnUnhandledRejections(false);
}]);
app.controller('ReviewController',['$scope','$http',function($scope,$http){
	this.product={};
	this.reviews=[]

	this.addreview = function(products){
		id=products.id
		var req = {
		method: 'PATCH',
 		url: 'http://127.0.0.1:8000/product/'+products.id+'/',
 		headers: {
   			'Content-Type': "application/json",
   			'X-CSRFToken': getCookie('csrftoken')
		},
 		data: products
		}
		console.log(products)
		$http(req).then(function(response){
			console.log(response)
		});
		products={}
	}
}]);
app.controller('addproductController',['$http',function($http){
	this.addproduct = function(item){
		var req = {
		method: 'POST',
 		url: 'http://127.0.0.1:8000/products/',
 		headers: {
   			'Content-Type': "application/json",
   			'X-CSRFToken': getCookie('csrftoken')
		},
 		data: item
		}
		console.log("item")
		console.log(item)
		$http(req).then(function(response){
			console.log(response)
		});
		prds={}
	};
}]);