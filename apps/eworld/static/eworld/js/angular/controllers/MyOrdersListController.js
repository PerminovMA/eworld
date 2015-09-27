/**
 * Created by PerminovMA@live.ru on 27.09.15.
 */

app.controller("MyOrdersListController",
    function ($scope, OrdersService) {
        $scope.getOrdersList = function () {
            OrdersService.query(
                {
                    get_only_my_orders: true
                },
                function (data) {
                    $scope.orders = data;
                },
                function (err_obj) {
                    alert("Произошла ошибка при получении списка заказов. Пожалуйста, попробуйте позже.")
                }
            );
        };

        $scope.getOrdersList();
    }
);