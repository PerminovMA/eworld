/**
 * Created by PerminovMA@live.ru on 11.08.15.
 */

app.controller("OrdersListController",
    function ($scope, OrdersService, CategoriesService) {

        $scope.orderTypes = CategoriesService.query();

        $scope.getAuctionsList = function () {
            if ($scope.sortOrder === 'undefined') {
                $scope.sortOrder = null;
            }
            if ($scope.selectedOrderType === 'undefined') {
                $scope.selectedOrderType = null;
            }

            OrdersService.query(
                {
                    sortOrder: $scope.sortOrder, selectedOrderType: $scope.selectedOrderType,
                    selectedCity: $scope.selectedCity
                },
                function (data) {
                    $scope.orders = data;
                },
                function (err_obj) {
                    alert("Произошла ошибка при получении списка аукционов. Пожалуйста, попробуйте позже.")
                }
            );
        };

        $scope.setOrderTypeSelected = function(orderType) {
            if (orderType != null) {  // not selected all types
                $scope.selectedOrderType = orderType.id;
            }
            else {
                $scope.selectedOrderType = null;
            }
            $scope.getAuctionsList();
        };

        $scope.getAuctionsList();
    }
);