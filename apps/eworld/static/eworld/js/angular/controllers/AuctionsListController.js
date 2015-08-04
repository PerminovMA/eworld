/**
 * Created by PerminovMA@live.ru on 19.07.15.
 */

app.controller("AuctionsListController",
    function ($scope, AuctionsService, CategoriesService) {

        $scope.orderTypes = CategoriesService.query();

        $scope.getAuctionsList = function () {
            if ($scope.sortOrder === 'undefined') {
                $scope.sortOrder = null;
            }
            if ($scope.selectedOrderType === 'undefined') {
                $scope.selectedOrderType = null;
            }

            AuctionsService.query({sortOrder: $scope.sortOrder, selectedOrderType: $scope.selectedOrderType,
                selectedCity: $scope.selectedCity},
                function(data) {
                    $scope.auctions = data;
                },
                function(err_obj){
                    alert("Произошла ошибка при получении списка аукционов. Пожалуйста, попробуйте позже.")
                });
        }

        $scope.setOrderTypeSelected = function(orderType) {
            if (orderType != null) {  // not selected all types
                $scope.selectedOrderType = orderType.id;
            }
            else {
                $scope.selectedOrderType = null;
            }
            $scope.getAuctionsList();
        }

        $scope.getAuctionsList();
    }
);