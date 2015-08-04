/**
 * Created by PerminovMA@live.ru on 04.08.15.
 */


filterModule = angular.module('eworldFilters', []);

filterModule.filter('moneyFormatter', function () {
    return function (input) {

        input = input.toString();
        if (input.length > 3) {
            var saved_length = input.length;
            for (var i = 0; i < saved_length; i++) {
                if (i % 3 === 0) {
                    var insert_pos = saved_length - i;

                    console.log(insert_pos);

                    if (insert_pos < saved_length) {
                        input = input.slice(0, insert_pos) + ' ' + input.slice(insert_pos);
                    }
                }
            }
        }
        return input;

    };
});