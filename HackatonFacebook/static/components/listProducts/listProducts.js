/**
 * Created by bustamante on 5/16/15.
 */

angular.module('HackathonApp').directive("listProducts", function(){
    return {
        restrict: 'E',
        scope: {
            recipes: '='
        },
        templateUrl: 'static/components/listProducts/listProducts.html',
        controller: function ($scope, Ajax) {
        }
    }
});

