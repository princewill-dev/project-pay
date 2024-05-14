(function ($) {
  /* "use strict" */

  var dzChartlist = (function () {
    let draw = Chart.controllers.line.__super__.draw; //draw shadow
    var screenWidth = $(window).width();

    var chartBar1 = function () {
      var options1 = {
          series: [
            {
              data: [
                25, 66, 41, 89, 63, 25, 44, 20, 36, 40, 54, 89, 63, 25, 80,
              ],
            },
          ],
          colors: ["#58BD7D"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          // labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },

          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },

          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
            marker: { show: !1 },
          },
          states: {
            hover: {
              filter: {
                type: "none",
                value: 0,
              },
            },
          },
        },
        chart1 = new ApexCharts(
          document.querySelector("#total-revenue-chart-1"),
          options1
        );
      chart1.render();
    };

    var chartBar2 = function () {
      var options2 = {
          series: [
            {
              data: [
                55, 56, 51, 49, 63, 35, 44, 40, 36, 40, 54, 49, 63, 35, 44, 3,
              ],
            },
          ],
          colors: ["#D33535"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },
          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },
          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
            marker: { show: !1 },
          },
        },
        chart2 = new ApexCharts(
          document.querySelector("#total-revenue-chart-2"),
          options2
        );
      chart2.render();
    };
    var chartBar3 = function () {
      var options2 = {
          series: [
            {
              data: [
                55, 56, 51, 49, 63, 35, 44, 40, 36, 40, 54, 49, 63, 35, 44, 3,
              ],
            },
          ],
          colors: ["#D33535"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },
          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },
          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
            marker: { show: !1 },
          },
        },
        chart2 = new ApexCharts(
          document.querySelector("#total-revenue-chart-3"),
          options2
        );
      chart2.render();
    };
    var chartBar4 = function () {
      var options1 = {
          series: [
            {
              data: [
                25, 66, 41, 89, 63, 25, 44, 20, 36, 40, 54, 89, 63, 25, 80,
              ],
            },
          ],
          colors: ["#58BD7D"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          // labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },

          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },

          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
            marker: { show: !1 },
          },
          states: {
            hover: {
              filter: {
                type: "none",
                value: 0,
              },
            },
          },
        },
        chart1 = new ApexCharts(
          document.querySelector("#total-revenue-chart-4"),
          options1
        );
      chart1.render();
    };
    var chartBar5 = function () {
      var options1 = {
          series: [
            {
              data: [
                25, 66, 41, 89, 63, 25, 44, 20, 36, 40, 54, 89, 63, 25, 80,
              ],
            },
          ],
          colors: ["#58BD7D"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          // labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },

          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },

          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
            marker: { show: !1 },
          },
          states: {
            hover: {
              filter: {
                type: "none",
                value: 0,
              },
            },
          },
        },
        chart1 = new ApexCharts(
          document.querySelector("#total-revenue-chart-5"),
          options1
        );
      chart1.render();
    };
    var chartBar6 = function () {
      var options2 = {
          series: [
            {
              data: [
                55, 56, 51, 49, 63, 35, 44, 40, 36, 40, 54, 49, 63, 35, 44, 3,
              ],
            },
          ],
          colors: ["#D33535"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },
          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },
          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
            marker: { show: !1 },
          },
        },
        chart2 = new ApexCharts(
          document.querySelector("#total-revenue-chart-6"),
          options2
        );
      chart2.render();
    };
    var chartBar7 = function () {
      var options1 = {
          series: [
            {
              data: [
                25, 66, 41, 89, 63, 25, 44, 20, 36, 40, 54, 89, 63, 25, 80,
              ],
            },
          ],
          colors: ["#58BD7D"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          // labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },

          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },

          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
            marker: { show: !1 },
          },
          states: {
            hover: {
              filter: {
                type: "none",
                value: 0,
              },
            },
          },
        },
        chart1 = new ApexCharts(
          document.querySelector("#total-revenue-chart-7"),
          options1
        );
      chart1.render();
    };
    var chartBar8 = function () {
      var options1 = {
          series: [
            {
              data: [
                25, 66, 41, 89, 63, 25, 44, 20, 36, 40, 54, 89, 63, 25, 80,
              ],
            },
          ],
          colors: ["#58BD7D"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          // labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },

          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },

          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
            marker: { show: !1 },
          },
          states: {
            hover: {
              filter: {
                type: "none",
                value: 0,
              },
            },
          },
        },
        chart1 = new ApexCharts(
          document.querySelector("#total-revenue-chart-8"),
          options1
        );
      chart1.render();
    };
    var chartBar9 = function () {
      var options1 = {
          series: [
            {
              data: [
                25, 66, 41, 89, 63, 25, 44, 20, 36, 40, 54, 89, 63, 25, 80,
              ],
            },
          ],
          colors: ["#58BD7D"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          // labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },

          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },

          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
            marker: { show: !1 },
          },
          states: {
            hover: {
              filter: {
                type: "none",
                value: 0,
              },
            },
          },
        },
        chart1 = new ApexCharts(
          document.querySelector("#total-revenue-chart-9"),
          options1
        );
      chart1.render();
    };

    var chartBar10 = function () {
      var options2 = {
          series: [
            {
              data: [
                55, 56, 51, 49, 63, 35, 44, 40, 36, 40, 54, 49, 63, 35, 44, 3,
              ],
            },
          ],
          colors: ["#D33535"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },
          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },
          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
            marker: { show: !1 },
          },
        },
        chart2 = new ApexCharts(
          document.querySelector("#total-revenue-chart-10"),
          options2
        );
      chart2.render();
    };
    var chartBar11 = function () {
      var options2 = {
          series: [
            {
              data: [
                55, 56, 51, 49, 63, 35, 44, 40, 36, 40, 54, 49, 63, 35, 44, 3,
              ],
            },
          ],
          colors: ["#D33535"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },
          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },
          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
            marker: { show: !1 },
          },
        },
        chart2 = new ApexCharts(
          document.querySelector("#total-revenue-chart-11"),
          options2
        );
      chart2.render();
    };
    var chartBar12 = function () {
      var options1 = {
          series: [
            {
              data: [
                25, 66, 41, 89, 63, 25, 44, 20, 36, 40, 54, 89, 63, 25, 80,
              ],
            },
          ],
          colors: ["#58BD7D"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          // labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },

          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },

          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
            marker: { show: !1 },
          },
          states: {
            hover: {
              filter: {
                type: "none",
                value: 0,
              },
            },
          },
        },
        chart1 = new ApexCharts(
          document.querySelector("#total-revenue-chart-12"),
          options1
        );
      chart1.render();
    };
    var chartBar13 = function () {
      var options1 = {
          series: [
            {
              data: [
                25, 66, 41, 89, 63, 25, 44, 20, 36, 40, 54, 89, 63, 25, 80,
              ],
            },
          ],
          colors: ["#58BD7D"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          // labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },

          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },

          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
            marker: { show: !1 },
          },
          states: {
            hover: {
              filter: {
                type: "none",
                value: 0,
              },
            },
          },
        },
        chart1 = new ApexCharts(
          document.querySelector("#total-revenue-chart-13"),
          options1
        );
      chart1.render();
    };
    var chartBar14 = function () {
      var options2 = {
          series: [
            {
              data: [
                55, 56, 51, 49, 63, 35, 44, 40, 36, 40, 54, 49, 63, 35, 44, 3,
              ],
            },
          ],
          colors: ["#D33535"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },
          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },
          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
            marker: { show: !1 },
          },
        },
        chart2 = new ApexCharts(
          document.querySelector("#total-revenue-chart-14"),
          options2
        );
      chart2.render();
    };
    var chartBar15 = function () {
      var options1 = {
          series: [
            {
              data: [
                25, 66, 41, 89, 63, 25, 44, 20, 36, 40, 54, 89, 63, 25, 80,
              ],
            },
          ],
          colors: ["#58BD7D"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          // labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },

          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },

          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
            marker: { show: !1 },
          },
          states: {
            hover: {
              filter: {
                type: "none",
                value: 0,
              },
            },
          },
        },
        chart1 = new ApexCharts(
          document.querySelector("#total-revenue-chart-15"),
          options1
        );
      chart1.render();
    };
    var chartBar16 = function () {
      var options1 = {
          series: [
            {
              data: [
                25, 66, 41, 89, 63, 25, 44, 20, 36, 40, 54, 89, 63, 25, 80,
              ],
            },
          ],
          colors: ["#58BD7D"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          // labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },

          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },

          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
            marker: { show: !1 },
          },
          states: {
            hover: {
              filter: {
                type: "none",
                value: 0,
              },
            },
          },
        },
        chart1 = new ApexCharts(
          document.querySelector("#total-revenue-chart-16"),
          options1
        );
      chart1.render();
    };
    var chartBar17 = function () {
      var options2 = {
          series: [
            {
              data: [
                55, 56, 51, 49, 63, 35, 44, 40, 36, 40, 54, 49, 63, 35, 44, 3,
              ],
            },
          ],
          colors: ["#D33535"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },
          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },
          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
            marker: { show: !1 },
          },
        },
        chart2 = new ApexCharts(
          document.querySelector("#total-revenue-chart-17"),
          options2
        );
      chart2.render();
    };
    var chartBar18 = function () {
      var options2 = {
          series: [
            {
              data: [
                55, 56, 51, 49, 63, 35, 44, 40, 36, 40, 54, 49, 63, 35, 44, 3,
              ],
            },
          ],
          colors: ["#D33535"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },
          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },
          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
            marker: { show: !1 },
          },
        },
        chart2 = new ApexCharts(
          document.querySelector("#total-revenue-chart-18"),
          options2
        );
      chart2.render();
    };
    var chartBar19 = function () {
      var options1 = {
          series: [
            {
              data: [
                25, 66, 41, 89, 63, 25, 44, 20, 36, 40, 54, 89, 63, 25, 80,
              ],
            },
          ],
          colors: ["#58BD7D"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          // labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },

          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },

          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
            marker: { show: !1 },
          },
          states: {
            hover: {
              filter: {
                type: "none",
                value: 0,
              },
            },
          },
        },
        chart1 = new ApexCharts(
          document.querySelector("#total-revenue-chart-19"),
          options1
        );
      chart1.render();
    };
    var chartBar20 = function () {
      var options1 = {
          series: [
            {
              data: [
                25, 66, 41, 89, 63, 25, 44, 20, 36, 40, 54, 89, 63, 25, 80,
              ],
            },
          ],
          colors: ["#58BD7D"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          // labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },

          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },

          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
            marker: { show: !1 },
          },
          states: {
            hover: {
              filter: {
                type: "none",
                value: 0,
              },
            },
          },
        },
        chart1 = new ApexCharts(
          document.querySelector("#total-revenue-chart-20"),
          options1
        );
      chart1.render();
    };
    var chartBar21 = function () {
      var options2 = {
          series: [
            {
              data: [
                55, 56, 51, 49, 63, 35, 44, 40, 36, 40, 54, 49, 63, 35, 44, 3,
              ],
            },
          ],
          colors: ["#D33535"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },
          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },
          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
            marker: { show: !1 },
          },
        },
        chart2 = new ApexCharts(
          document.querySelector("#total-revenue-chart-21"),
          options2
        );
      chart2.render();
    };
    var chartBar22 = function () {
      var options1 = {
          series: [
            {
              data: [
                25, 66, 41, 89, 63, 25, 44, 20, 36, 40, 54, 89, 63, 25, 80,
              ],
            },
          ],
          colors: ["#58BD7D"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          // labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },

          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },

          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
            marker: { show: !1 },
          },
          states: {
            hover: {
              filter: {
                type: "none",
                value: 0,
              },
            },
          },
        },
        chart1 = new ApexCharts(
          document.querySelector("#total-revenue-chart-22"),
          options1
        );
      chart1.render();
    };
    var chartBar23 = function () {
      var options1 = {
          series: [
            {
              data: [
                25, 66, 41, 89, 63, 25, 44, 20, 36, 40, 54, 89, 63, 25, 80,
              ],
            },
          ],
          colors: ["#58BD7D"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          // labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },

          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },

          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
            marker: { show: !1 },
          },
          states: {
            hover: {
              filter: {
                type: "none",
                value: 0,
              },
            },
          },
        },
        chart1 = new ApexCharts(
          document.querySelector("#total-revenue-chart-23"),
          options1
        );
      chart1.render();
    };
    var chartBar24 = function () {
      var options1 = {
          series: [
            {
              data: [
                25, 66, 41, 89, 63, 25, 44, 20, 36, 40, 54, 89, 63, 25, 80,
              ],
            },
          ],
          colors: ["#58BD7D"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          // labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },

          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },

          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
            marker: { show: !1 },
          },
          states: {
            hover: {
              filter: {
                type: "none",
                value: 0,
              },
            },
          },
        },
        chart1 = new ApexCharts(
          document.querySelector("#total-revenue-chart-24"),
          options1
        );
      chart1.render();
    };
    var chartBar25 = function () {
      var options1 = {
          series: [
            {
              data: [
                25, 66, 41, 89, 63, 25, 44, 20, 36, 40, 54, 89, 63, 25, 80,
              ],
            },
          ],
          colors: ["#58BD7D"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          // labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },

          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },

          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
            marker: { show: !1 },
          },
          states: {
            hover: {
              filter: {
                type: "none",
                value: 0,
              },
            },
          },
        },
        chart1 = new ApexCharts(
          document.querySelector("#total-revenue-chart-25"),
          options1
        );
      chart1.render();
    };
    var chartBar26 = function () {
      var options1 = {
          series: [
            {
              data: [
                25, 66, 41, 89, 63, 25, 44, 20, 36, 40, 54, 89, 63, 25, 80,
              ],
            },
          ],
          colors: ["#58BD7D"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          // labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },

          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },

          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
            marker: { show: !1 },
          },
          states: {
            hover: {
              filter: {
                type: "none",
                value: 0,
              },
            },
          },
        },
        chart1 = new ApexCharts(
          document.querySelector("#total-revenue-chart-26"),
          options1
        );
      chart1.render();
    };
    var chartBar27 = function () {
      var options1 = {
          series: [
            {
              data: [
                25, 66, 41, 89, 63, 25, 44, 20, 36, 40, 54, 89, 63, 25, 80,
              ],
            },
          ],
          colors: ["#58BD7D"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          // labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },

          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },

          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
            marker: { show: !1 },
          },
          states: {
            hover: {
              filter: {
                type: "none",
                value: 0,
              },
            },
          },
        },
        chart1 = new ApexCharts(
          document.querySelector("#total-revenue-chart-27"),
          options1
        );
      chart1.render();
    };
    var chartBar28 = function () {
      var options1 = {
          series: [
            {
              data: [
                25, 66, 41, 89, 63, 25, 44, 20, 36, 40, 54, 89, 63, 25, 80,
              ],
            },
          ],
          colors: ["#58BD7D"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          // labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },

          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },

          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
            marker: { show: !1 },
          },
          states: {
            hover: {
              filter: {
                type: "none",
                value: 0,
              },
            },
          },
        },
        chart1 = new ApexCharts(
          document.querySelector("#total-revenue-chart-28"),
          options1
        );
      chart1.render();
    };
    var chartBar29 = function () {
      var options1 = {
          series: [
            {
              data: [
                25, 66, 41, 89, 63, 25, 44, 20, 36, 40, 54, 89, 63, 25, 80,
              ],
            },
          ],
          colors: ["#58BD7D"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          // labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },

          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },

          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
            marker: { show: !1 },
          },
          states: {
            hover: {
              filter: {
                type: "none",
                value: 0,
              },
            },
          },
        },
        chart1 = new ApexCharts(
          document.querySelector("#total-revenue-chart-29"),
          options1
        );
      chart1.render();
    };
    var chartBar30 = function () {
      var options1 = {
          series: [
            {
              data: [
                25, 66, 41, 89, 63, 25, 44, 20, 36, 40, 54, 89, 63, 25, 80,
              ],
            },
          ],
          colors: ["#58BD7D"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          // labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },

          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },

          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
            marker: { show: !1 },
          },
          states: {
            hover: {
              filter: {
                type: "none",
                value: 0,
              },
            },
          },
        },
        chart1 = new ApexCharts(
          document.querySelector("#total-revenue-chart-30"),
          options1
        );
      chart1.render();
    };
    var chartBar31 = function () {
      var options1 = {
          series: [
            {
              data: [
                25, 66, 41, 89, 63, 25, 44, 20, 36, 40, 54, 89, 63, 25, 80,
              ],
            },
          ],
          colors: ["#58BD7D"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          // labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },

          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },

          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
            marker: { show: !1 },
          },
          states: {
            hover: {
              filter: {
                type: "none",
                value: 0,
              },
            },
          },
        },
        chart1 = new ApexCharts(
          document.querySelector("#total-revenue-chart-31"),
          options1
        );
      chart1.render();
    };
    var chartBar32 = function () {
      var options1 = {
          series: [
            {
              data: [
                25, 66, 41, 89, 63, 25, 44, 20, 36, 40, 54, 89, 63, 25, 80,
              ],
            },
          ],
          colors: ["#58BD7D"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          // labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },

          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },

          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
            marker: { show: !1 },
          },
          states: {
            hover: {
              filter: {
                type: "none",
                value: 0,
              },
            },
          },
        },
        chart1 = new ApexCharts(
          document.querySelector("#total-revenue-chart-32"),
          options1
        );
      chart1.render();
    };
    var chartBar33 = function () {
      var options1 = {
          series: [
            {
              data: [
                25, 66, 41, 89, 63, 25, 44, 20, 36, 40, 54, 89, 63, 25, 80,
              ],
            },
          ],
          colors: ["#58BD7D"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          // labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },

          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },

          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
            marker: { show: !1 },
          },
          states: {
            hover: {
              filter: {
                type: "none",
                value: 0,
              },
            },
          },
        },
        chart1 = new ApexCharts(
          document.querySelector("#total-revenue-chart-33"),
          options1
        );
      chart1.render();
    };
    var chartBar34 = function () {
      var options1 = {
          series: [
            {
              data: [
                25, 66, 41, 89, 63, 25, 44, 20, 36, 40, 54, 89, 63, 25, 80,
              ],
            },
          ],
          colors: ["#58BD7D"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          // labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },

          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },

          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
            marker: { show: !1 },
          },
          states: {
            hover: {
              filter: {
                type: "none",
                value: 0,
              },
            },
          },
        },
        chart1 = new ApexCharts(
          document.querySelector("#total-revenue-chart-34"),
          options1
        );
      chart1.render();
    };
    var chartBar35 = function () {
      var options2 = {
          series: [
            {
              data: [
                55, 56, 51, 49, 63, 35, 44, 40, 36, 40, 54, 49, 63, 35, 44, 3,
              ],
            },
          ],
          colors: ["#D33535"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },
          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },
          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
            marker: { show: !1 },
          },
        },
        chart2 = new ApexCharts(
          document.querySelector("#total-revenue-chart-35"),
          options2
        );
      chart2.render();
    };
    var chartBar36 = function () {
      var options2 = {
          series: [
            {
              data: [
                55, 56, 51, 49, 63, 35, 44, 40, 36, 40, 54, 49, 63, 35, 44, 3,
              ],
            },
          ],
          colors: ["#D33535"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },
          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },
          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
            marker: { show: !1 },
          },
        },
        chart2 = new ApexCharts(
          document.querySelector("#total-revenue-chart-36"),
          options2
        );
      chart2.render();
    };
    var chartBar37 = function () {
      var options1 = {
          series: [
            {
              data: [
                25, 66, 41, 89, 63, 25, 44, 20, 36, 40, 54, 89, 63, 25, 80,
              ],
            },
          ],
          colors: ["#58BD7D"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          // labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },

          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },

          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
            marker: { show: !1 },
          },
          states: {
            hover: {
              filter: {
                type: "none",
                value: 0,
              },
            },
          },
        },
        chart1 = new ApexCharts(
          document.querySelector("#total-revenue-chart-37"),
          options1
        );
      chart1.render();
    };
    var chartBar38 = function () {
      var options1 = {
          series: [
            {
              data: [
                25, 66, 41, 89, 63, 25, 44, 20, 36, 40, 54, 89, 63, 25, 80,
              ],
            },
          ],
          colors: ["#58BD7D"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          // labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },

          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },

          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
            marker: { show: !1 },
          },
          states: {
            hover: {
              filter: {
                type: "none",
                value: 0,
              },
            },
          },
        },
        chart1 = new ApexCharts(
          document.querySelector("#total-revenue-chart-38"),
          options1
        );
      chart1.render();
    };
    var chartBar39 = function () {
      var options1 = {
          series: [
            {
              data: [
                25, 66, 41, 89, 63, 25, 44, 20, 36, 40, 54, 89, 63, 25, 80,
              ],
            },
          ],
          colors: ["#58BD7D"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          // labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },

          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },

          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
            marker: { show: !1 },
          },
          states: {
            hover: {
              filter: {
                type: "none",
                value: 0,
              },
            },
          },
        },
        chart1 = new ApexCharts(
          document.querySelector("#total-revenue-chart-39"),
          options1
        );
      chart1.render();
    };
    var chartBar40 = function () {
      var options2 = {
          series: [
            {
              data: [
                55, 56, 51, 49, 63, 35, 44, 40, 36, 40, 54, 49, 63, 35, 44, 3,
              ],
            },
          ],
          colors: ["#D33535"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },
          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },
          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
            marker: { show: !1 },
          },
        },
        chart2 = new ApexCharts(
          document.querySelector("#total-revenue-chart-40"),
          options2
        );
      chart2.render();
    };
    var chartBar41 = function () {
      var options2 = {
          series: [
            {
              data: [
                55, 56, 51, 49, 63, 35, 44, 40, 36, 40, 54, 49, 63, 35, 44, 3,
              ],
            },
          ],
          colors: ["#D33535"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },
          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },
          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
            marker: { show: !1 },
          },
        },
        chart2 = new ApexCharts(
          document.querySelector("#total-revenue-chart-41"),
          options2
        );
      chart2.render();
    };
    var chartBar42 = function () {
      var options1 = {
          series: [
            {
              data: [
                25, 66, 41, 89, 63, 25, 44, 20, 36, 40, 54, 89, 63, 25, 80,
              ],
            },
          ],
          colors: ["#58BD7D"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          // labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },

          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },

          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
            marker: { show: !1 },
          },
          states: {
            hover: {
              filter: {
                type: "none",
                value: 0,
              },
            },
          },
        },
        chart1 = new ApexCharts(
          document.querySelector("#total-revenue-chart-42"),
          options1
        );
      chart1.render();
    };
    var chartBar43 = function () {
      var options1 = {
          series: [
            {
              data: [
                25, 66, 41, 89, 63, 25, 44, 20, 36, 40, 54, 89, 63, 25, 80,
              ],
            },
          ],
          colors: ["#58BD7D"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          // labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },

          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },

          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
            marker: { show: !1 },
          },
          states: {
            hover: {
              filter: {
                type: "none",
                value: 0,
              },
            },
          },
        },
        chart1 = new ApexCharts(
          document.querySelector("#total-revenue-chart-43"),
          options1
        );
      chart1.render();
    };
    var chartBar44 = function () {
      var options1 = {
          series: [
            {
              data: [
                25, 66, 41, 89, 63, 25, 44, 20, 36, 40, 54, 89, 63, 25, 80,
              ],
            },
          ],
          colors: ["#58BD7D"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          // labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },

          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },

          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
            marker: { show: !1 },
          },
          states: {
            hover: {
              filter: {
                type: "none",
                value: 0,
              },
            },
          },
        },
        chart1 = new ApexCharts(
          document.querySelector("#total-revenue-chart-44"),
          options1
        );
      chart1.render();
    };
    var chartBar45 = function () {
      var options2 = {
          series: [
            {
              data: [
                55, 56, 51, 49, 63, 35, 44, 40, 36, 40, 54, 49, 63, 35, 44, 3,
              ],
            },
          ],
          colors: ["#D33535"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },
          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },
          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
            marker: { show: !1 },
          },
        },
        chart2 = new ApexCharts(
          document.querySelector("#total-revenue-chart-45"),
          options2
        );
      chart2.render();
    };
    var chartBar46 = function () {
      var options2 = {
          series: [
            {
              data: [
                55, 56, 51, 49, 63, 35, 44, 40, 36, 40, 54, 49, 63, 35, 44, 3,
              ],
            },
          ],
          colors: ["#D33535"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },
          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },
          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
            marker: { show: !1 },
          },
        },
        chart2 = new ApexCharts(
          document.querySelector("#total-revenue-chart-46"),
          options2
        );
      chart2.render();
    };
    var chartBar47 = function () {
      var options1 = {
          series: [
            {
              data: [
                25, 66, 41, 89, 63, 25, 44, 20, 36, 40, 54, 89, 63, 25, 80,
              ],
            },
          ],
          colors: ["#58BD7D"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          // labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },

          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },

          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
            marker: { show: !1 },
          },
          states: {
            hover: {
              filter: {
                type: "none",
                value: 0,
              },
            },
          },
        },
        chart1 = new ApexCharts(
          document.querySelector("#total-revenue-chart-47"),
          options1
        );
      chart1.render();
    };
    var chartBar48 = function () {
      var options1 = {
          series: [
            {
              data: [
                25, 66, 41, 89, 63, 25, 44, 20, 36, 40, 54, 89, 63, 25, 80,
              ],
            },
          ],
          colors: ["#58BD7D"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          // labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },

          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },

          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
            marker: { show: !1 },
          },
          states: {
            hover: {
              filter: {
                type: "none",
                value: 0,
              },
            },
          },
        },
        chart1 = new ApexCharts(
          document.querySelector("#total-revenue-chart-48"),
          options1
        );
      chart1.render();
    };
    var chartBar49 = function () {
      var options1 = {
          series: [
            {
              data: [
                25, 66, 41, 89, 63, 25, 44, 20, 36, 40, 54, 89, 63, 25, 80,
              ],
            },
          ],
          colors: ["#58BD7D"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          // labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },

          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },

          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
            marker: { show: !1 },
          },
          states: {
            hover: {
              filter: {
                type: "none",
                value: 0,
              },
            },
          },
        },
        chart1 = new ApexCharts(
          document.querySelector("#total-revenue-chart-49"),
          options1
        );
      chart1.render();
    };
    var chartBar50 = function () {
      var options1 = {
          series: [
            {
              data: [
                25, 66, 41, 89, 63, 25, 44, 20, 36, 40, 54, 89, 63, 25, 80,
              ],
            },
          ],
          colors: ["#58BD7D"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          // labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },

          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },

          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
            marker: { show: !1 },
          },
          states: {
            hover: {
              filter: {
                type: "none",
                value: 0,
              },
            },
          },
        },
        chart1 = new ApexCharts(
          document.querySelector("#total-revenue-chart-50"),
          options1
        );
      chart1.render();
    };
    var chartBar51 = function () {
      var options2 = {
          series: [
            {
              data: [
                55, 56, 51, 49, 63, 35, 44, 40, 36, 40, 54, 49, 63, 35, 44, 3,
              ],
            },
          ],
          colors: ["#D33535"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },
          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },
          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
            marker: { show: !1 },
          },
        },
        chart2 = new ApexCharts(
          document.querySelector("#total-revenue-chart-51"),
          options2
        );
      chart2.render();
    };
    var chartBar52 = function () {
      var options2 = {
          series: [
            {
              data: [
                55, 56, 51, 49, 63, 35, 44, 40, 36, 40, 54, 49, 63, 35, 44, 3,
              ],
            },
          ],
          colors: ["#D33535"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },
          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },
          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
            marker: { show: !1 },
          },
        },
        chart2 = new ApexCharts(
          document.querySelector("#total-revenue-chart-52"),
          options2
        );
      chart2.render();
    };
    var chartBar53 = function () {
      var options1 = {
          series: [
            {
              data: [
                25, 66, 41, 89, 63, 25, 44, 20, 36, 40, 54, 89, 63, 25, 80,
              ],
            },
          ],
          colors: ["#58BD7D"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          // labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },

          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },

          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
            marker: { show: !1 },
          },
          states: {
            hover: {
              filter: {
                type: "none",
                value: 0,
              },
            },
          },
        },
        chart1 = new ApexCharts(
          document.querySelector("#total-revenue-chart-53"),
          options1
        );
      chart1.render();
    };
    var chartBar54 = function () {
      var options1 = {
          series: [
            {
              data: [
                25, 66, 41, 89, 63, 25, 44, 20, 36, 40, 54, 89, 63, 25, 80,
              ],
            },
          ],
          colors: ["#58BD7D"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          // labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },

          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },

          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
            marker: { show: !1 },
          },
          states: {
            hover: {
              filter: {
                type: "none",
                value: 0,
              },
            },
          },
        },
        chart1 = new ApexCharts(
          document.querySelector("#total-revenue-chart-54"),
          options1
        );
      chart1.render();
    };
    var chartBar55 = function () {
      var options2 = {
          series: [
            {
              data: [
                55, 56, 51, 49, 63, 35, 44, 40, 36, 40, 54, 49, 63, 35, 44, 3,
              ],
            },
          ],
          colors: ["#D33535"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },
          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },
          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
            marker: { show: !1 },
          },
        },
        chart2 = new ApexCharts(
          document.querySelector("#total-revenue-chart-55"),
          options2
        );
      chart2.render();
    };
    var chartBar56 = function () {
      var options2 = {
          series: [
            {
              data: [
                55, 56, 51, 49, 63, 35, 44, 40, 36, 40, 54, 49, 63, 35, 44, 3,
              ],
            },
          ],
          colors: ["#D33535"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },
          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },
          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
            marker: { show: !1 },
          },
        },
        chart2 = new ApexCharts(
          document.querySelector("#total-revenue-chart-56"),
          options2
        );
      chart2.render();
    };
    var chartBar57 = function () {
      var options1 = {
          series: [
            {
              data: [
                25, 66, 41, 89, 63, 25, 44, 20, 36, 40, 54, 89, 63, 25, 80,
              ],
            },
          ],
          colors: ["#58BD7D"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          // labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },

          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },

          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
            marker: { show: !1 },
          },
          states: {
            hover: {
              filter: {
                type: "none",
                value: 0,
              },
            },
          },
        },
        chart1 = new ApexCharts(
          document.querySelector("#total-revenue-chart-57"),
          options1
        );
      chart1.render();
    };
    var chartBar58 = function () {
      var options2 = {
          series: [
            {
              data: [
                55, 56, 51, 49, 63, 35, 44, 40, 36, 40, 54, 49, 63, 35, 44, 3,
              ],
            },
          ],
          colors: ["#D33535"],
          chart: {
            type: "area",
            width: 100,
            height: 40,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },
          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },
          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
            marker: { show: !1 },
          },
        },
        chart2 = new ApexCharts(
          document.querySelector("#total-revenue-chart-58"),
          options2
        );
      chart2.render();
    };

    var chartBar59 = function () {
      var options2 = {
          series: [
            {
              data: [
                6, 12, 30, 55, 20, 51, 49, 63, 35, 44, 40, 36, 40, 54, 49, 63,
                35, 44, 3,
              ],
            },
          ],
          colors: ["#D33535"],
          chart: {
            type: "area",
            width: 506,
            height: 100,
            sparkline: { enabled: !0 },
          },
          plotOptions: { bar: { columnWidth: "50%" } },
          labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
          xaxis: { crosshairs: { width: 1 } },
          stroke: {
            show: true,
            curve: "smooth",
            lineCap: "butt",
            colors: undefined,
            width: 2,
            dashArray: 0,
          },
          tooltip: {
            fixed: { enabled: !1 },
            x: { show: !1 },
            y: {
              title: {
                formatter: function (e) {
                  return "";
                },
              },
            },
            marker: { show: !1 },
          },
        },
        chart2 = new ApexCharts(
          document.querySelector("#total-revenue-chart-59"),
          options2
        );
      chart2.render();
    };

    /* Function ============ */
    return {
      init: function () {},

      load: function () {
        chartBar1();
        chartBar2();
        chartBar3();
        chartBar4();
        chartBar5();
        chartBar6();
        chartBar7();
        chartBar8();
        chartBar9();
        chartBar10();
        chartBar11();
        chartBar12();
        chartBar13();
        chartBar14();
        chartBar15();
        chartBar16();
        chartBar17();
        chartBar18();
        chartBar19();
        chartBar20();
        chartBar21();
        chartBar22();
        chartBar23();
        chartBar24();
        chartBar25();
        chartBar26();
        chartBar27();
        chartBar28();
        chartBar29();
        chartBar30();
        chartBar31();
        chartBar32();
        chartBar33();
        chartBar34();
        chartBar35();
        chartBar36();
        chartBar37();
        chartBar38();
        chartBar39();
        chartBar40();
        chartBar41();
        chartBar42();
        chartBar43();
        chartBar44();
        chartBar45();
        chartBar46();
        chartBar47();
        chartBar48();
        chartBar49();
        chartBar50();
        chartBar51();
        chartBar52();
        chartBar53();
        chartBar54();
        chartBar55();
        chartBar56();
        chartBar57();
        chartBar58();
        chartBar59();
      },

      resize: function () {},
    };
  })();

  jQuery(document).ready(function () {});

  jQuery(window).on("load", function () {
    setTimeout(function () {
      dzChartlist.load();
    }, 1000);
  });

  jQuery(window).on("resize", function () {});
})(jQuery);
