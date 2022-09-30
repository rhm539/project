/**
 * Fixed Table Header Plugin for jQuery
 *
 * @version 1.0.0
 * @license MIT
 * @author Kiyofumi Torigoe (kiyotd, torigoedesign)
 * @copyright 2021 Kiyofumi Torigoe
 */
(function ($) {

  const defaultTarget = "th";

  const defaultCss = {
    position: "sticky",
    top: 0,
    background: "#17a2b8",
    color: "#fff"
  };

  $.fn.fixedTableHeader = function (target = null, css = null) {

    target = target ?? defaultTarget;
    css = css ?? defaultCss;

    const resultCss = Object.assign({}, defaultCss, css)
    // const resultCss = { ...defaultCss, ...css }

    $(target, this).css(resultCss);
    return this;

  }
})(jQuery);
