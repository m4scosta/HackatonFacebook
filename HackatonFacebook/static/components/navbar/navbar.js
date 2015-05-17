/**
 * Created by bustamante on 5/16/15.
 */

angular.module('HackathonApp').directive('navbarHack', function(){
    return {
        restrict: 'E',
        templateUrl: 'static/components/navbar/navbar.html',
        controller: function($scope, $window){

        	$scope.login = function() {
        		if ($window.FB !== undefined) {
        			$window.FB.getLoginStatus(function (response) {
        				$window.FB.getLoginStatus(function (response) {
	                        if (response.status !== "connected")  {
	                            FB.login(function(response) {}, {
	                               scope: 'publish_actions', 
	                               return_scopes: true
	                            });
	                        }
	                    });
        			});
        		}
        	}
        }
    }
});
