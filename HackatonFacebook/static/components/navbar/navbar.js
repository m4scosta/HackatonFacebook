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
	                            $window.FB.login(function(response) {}, {
	                               scope: 'publish_actions', 
	                               return_scopes: true
	                            });
	                        }
	                    });
        			});
        		}
        	}
            $scope.picture;
            $scope.$watch(function() {
                return $window.FB;
            }, function () {
                if ($window.FB !== undefined) {
                    $window.FB.getLoginStatus(function (response) {
                        $window.FB.getLoginStatus(function (response) {
                            if (response.status === "connected")  {
                                $window.FB.api("/me", "get", {"fields": "picture,name"}, function (response) {
                                    if (!response || response.error) {
                                        console.log("error while requesting profile picture");
                                    } else {

                                        $scope.user = response;
                                        $scope.$digest()
                                    }
                                });
                            }
                        });
                    });
                }
            });
        }
    }
});
