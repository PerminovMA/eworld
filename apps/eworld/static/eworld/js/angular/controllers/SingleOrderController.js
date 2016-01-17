/**
 * Created by PerminovMA@live.ru on 17.01.16.
 */


app.controller("SingleOrderController",
    function ($scope, OrdersService, $modal, URLs, $interval) {
        $scope.updateComments = function () {
            OrdersService.get_comments(
                {
                    order_id: ORDER_ID
                },
                function (data) {
                    $scope.comments = data;
                },
                function (err_obj) {
                    console.log(err_obj);
                    alert("Произошла ошибка при получении комментариев, обратитесь к администратору сайта.");
                }
            );
        };

        $scope.updateComments();

        $scope.make_comment = function () {
            if (!this.new_comment_text) {
                alert("Введите текст.");
                return;
            }

            OrdersService.make_comment(
                {
                    id: ORDER_ID,  // variable ORDER_ID is taken from HTML template
                    text: this.new_comment_text
                },
                function (data) {
                    if (data.result != "success") {
                        alert("Произошла ошибка при отправке комментария: " + data.message);
                    }
                    $scope.updateComments();
                },
                function (err_obj) {
                    console.log(err_obj);
                    alert("Произошла ошибка при отправке комментария: " + err_obj);
                }
            );
            this.new_comment_text = '';
        };

    });
