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

                    if (insert_pos < saved_length) {
                        input = input.slice(0, insert_pos) + ' ' + input.slice(insert_pos);
                    }
                }
            }
        }
        return input;

    };
});

// return only first city from cities set. ( input example: "cities": [{"name": "Moscow"}]
// return example: "Moscow"
filterModule.filter('firstCity', function () {
    return function (input) {
        if (input.length) {
            return input[0].name;
        } else {
            return '';
        }
    };
});

// return all cities as string from cities set. ( input example: "cities": [{"name": "Moscow"}, {"name": "SPb"}]
// return example: "Moscow, SPb"
filterModule.filter('allCities', function () {
    return function (input) {
        var result = "";
        for (var i = 0; i < input.length; i++) {
            result += input[i].name + ', ';
        }
        return result.slice(0, -2);
    };
});