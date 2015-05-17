/**
 * Created by bustamante on 5/16/15.
 */

angular.module('HackathonApp').directive("listProducts", function(){
    return {
        restrict: 'E',
        scope: {
            recipes: '=',
            viewproduct: '=',
            openproduct: '='
        },
        templateUrl: 'static/components/listProducts/listProducts.html',
        controller: function ($scope) {
            $scope.openProduct = function(index){
                $scope.openproduct = $scope.recipes[index];
                $scope.viewproduct = true;
            };

            $scope.myOrder = function(recipe, recipe2){
                return recipe.count_have - recipe.count_no_have
            }
        }
    }
});
