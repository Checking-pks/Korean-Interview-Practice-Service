def returnCss():
    return """
<style>
#gauge, #radar {
  width: calc(50% - 20px);
  height: calc(100% - 89px - 40px) !important;
  min-height: 379px;
  margin: 20px;
}

pre {
  white-space: pre-wrap;
}

.u-table tr:not(:last-child) {
  border-bottom: 0.01em solid #eeeeee;
}

.u-text-result-number {
  font-size: 35px;
  margin-bottom: 15px;
  font-weight: bold;
}

.u-text-result-reply {
  font-size: 15px;
}

.u-text-3 {
  font-weight: bold;
  font-size: 4.5em;

  margin: auto;
}

.u-text-4 {
  font-size: 30px;
  font-weight: bold;
}

.u-margin-left-auto-right-10px {
  margin-left: auto;
  margin-right: 10px;
}

.u-margin-top-bottom-auto {
  margin-top: auto;
  margin-bottom: auto;
}

.u-text .u-text-table-score-1 {
  font-size: 30px;
  font-weight: bold;
  width: 0;
}

.u-text .u-text-table-score-2 {
  font-size: 13px;
  vertical-align: bottom;
  padding: 10px;
}

.u-list-flex-row {
  flex-direction: row !important;
}

.u-section-1 {
  background-image: none;
}

.u-section-1 .u-sheet-1 {
  min-height: 1039px;
}

.u-section-1 .u-group-1 {
  min-height: 403px;
  margin: 20px 0 60px auto;
}

.u-section-1 .u-shape-1 {
  width: 801px;
  height: 552px;
  margin: 204px auto 0 118px;
}

.u-section-1 .u-text-1 {
  font-family: Cambay;
  font-weight: 700;
  font-size: 3.75rem;
  margin: 70px auto 0;
}

.u-section-1 .u-text-2 {
  width: 749px;
  font-size: 1.125rem;
  margin: 20px auto 0;
}

.u-section-1 .u-list-1 {
  grid-template-rows: auto;
  margin-top: 89px;
}

.u-section-1 .u-repeater-1 {
  grid-gap: 0px 0px;
}

.u-section-1 .u-list-2 {
  margin: 81px 0 0 auto;
}

.u-section-1 .u-repeater-2 {
  grid-template-columns: 100%;
  min-height: 379px;
  grid-gap: 22px 22px;
}

.u-section-1 .u-list-item-1 {
  box-shadow: 5px 5px 20px 0 rgba(0,0,0,0.1);
  background-image: none;
}

.u-section-1 .u-container-layout-1 {
  padding: 30px 60px 60px 60px;
}

.u-section-1 .u-list-3 {
  margin-top: 129px;
  margin-bottom: 60px;
}

.u-section-1 .u-repeater-3 {
  grid-template-columns: 100%;
  min-height: 330px;
  grid-gap: 22px 22px;
}

.u-section-1 .u-list-item-2 {
  box-shadow: 5px 5px 20px 0 rgba(0,0,0,0.1);
  background-image: none;
  padding-bottom: 20px;
}

.u-section-1 .u-container-layout-2 {
  padding: 30px 20px;
}

@media (max-width: 1199px) {
  .u-section-1 .u-repeater-1 {
    grid-template-columns: repeat(undefined, NaN%);
  }
}

@media (max-width: 991px) {
  .u-section-1 .u-text-2 {
    width: 720px;
  }

  .u-section-1 .u-repeater-1 {
    grid-template-columns: 100%;
  }
}

@media (max-width: 767px) {
  .u-section-1 .u-text-2 {
    width: 540px;
  }

  .u-section-1 .u-container-layout-1 {
    padding-left: 10px;
    padding-right: 10px;
  }

  .u-section-1 .u-container-layout-2 {
    padding-left: 10px;
    padding-right: 10px;
  }
}

@media (max-width: 575px) {
  .u-section-1 .u-text-1 {
    font-size: 2.25rem;
  }

  .u-section-1 .u-text-2 {
    width: 340px;
  }
}
</style>"""