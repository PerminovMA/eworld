/**
 * Created by PerminovMA@live.ru on 08.08.15.
 */

app.controller("MyAuctionsListController",
    function ($scope, AuctionsService) {
        $scope.getAuctionsList = function () {
            AuctionsService.query(
                {
                    get_only_my_auctions: true
                },
                function (data) {
                    $scope.auctions = data;
                },
                function (err_obj) {
                    alert("Произошла ошибка при получении списка аукционов. Пожалуйста, попробуйте позже.")
                }
            );
        };

        $scope.getAuctionsList();
    }
);