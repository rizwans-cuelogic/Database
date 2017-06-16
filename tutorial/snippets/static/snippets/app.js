var app = angular.module("app", []);
app.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('//');
    $interpolateProvider.endSymbol('//');
    //$httpProvider.defaults.xsrfCookieName='csrf'
    //$httpProvider.defaults.xsrfHeaderName='X-CSRFToken'
    //$resourceProvider.defaults.stripTrailingSlashes=false;
  });
// app.directive('bannerText',function(){
// 	return{
// 		restrict:'E',
// 		templateUrl:'banner-text.html'
// 	};
// });