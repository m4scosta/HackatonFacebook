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
            $scope.recipes = [];
            for(var i = 0; i < 20; ++i) {
                $scope.recipes.push(
                    {
                        name: 'Torta de Morango',
                        photo: 'static/images/servelet.png',
                        preparation: ['adsfadsf'],
                        prepare_time: '',
                        income: '',
                        ingredients: ['a', 'b'],
                        ingredients_in: ['a', 'b'],
                        ingredients_out: ['c']
                    }
                )
            }
        }
    }
});

