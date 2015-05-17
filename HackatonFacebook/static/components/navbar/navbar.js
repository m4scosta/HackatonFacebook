/**
 * Created by bustamante on 5/16/15.
 */

angular.module('HackathonApp').directive('navbarHack', function(){
    return {
        restrict: 'E',
        templateUrl: 'static/components/navbar/navbar.html',
        link: function(element, attr, scope){
        }
    }
});
