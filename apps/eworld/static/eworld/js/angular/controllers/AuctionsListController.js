/**
 * Created by PerminovMA@live.ru on 19.07.15.
 */

app.factory('Auctions', [
    '$resource', function($resource) {
        return $resource('eworld/rest_api/auctions_data/', {});
    }
]);

app.controller("AuctionsListController",
    function ($scope, URLs, Auctions) {
        $scope.namee = "Mihail Perminov";

        $scope.orderTypes = [
                                {id: 1, name: 'Музыканты, артисты, dj', className: 'ew-icon-music'},
                                {id: 2, name: 'Транспорт, Свадебные Лимузины', className: 'ew-icon-transport'},
                                {id: 3, name: 'Видеосьёмка', className: ''},
                                {id: 4, name: 'Стилисты', className: ''},
                                {id: 5, name: 'Ювелирные изделия', className: ''},
                                {id: 6, name: 'Рестораны', className: ''},
                                {id: 1, name: 'Места прогулок', className: ''},
                                {id: 1, name: 'Тепоходы', className: ''},
                                {id: 1, name: 'Свадебные платья', className: ''},
                                {id: 1, name: 'Реквизиты для меропреятий', className: ''},
                                {id: 1, name: 'Отели', className: ''},
                                {id: 1, name: 'Кейтеринг', className: ''},
                                {id: 1, name: 'Меропреятия за границей', className: ''},
                                {id: 1, name: 'Заказ букетов', className: ''},
                                {id: 1, name: 'Оформление помещений', className: ''},
                                {id: 1, name: 'Свадьба, Венчание', className: ''},
                                {id: 1, name: 'Заказ тортов', className: ''},
                            ];

        $scope.getAuctionsList = function () {
            if ($scope.sortOrder === 'undefined') {
                $scope.sortOrder = null;
            }
            if ($scope.selectedOrderType === 'undefined') {
                $scope.selectedOrderType = null;
            }

            Auctions.query({sortOrder: $scope.sortOrder, selectedOrderType: $scope.selectedOrderType,
                selectedCity: $scope.selectedCity},
                function(data) {
                    $scope.auctions = data;
                    console.log(data);
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

        //$scope.$watch('auctionCategory', function(newValue, oldValue) {
        //    alert($scope.auctionCategory);
        //});
    }
);