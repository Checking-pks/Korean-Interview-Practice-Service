def returnCss():
    return """
<style>
.stTextArea {
	margin: 20px auto;
	width: 50% !important;
}

textarea {
  resize: none !important;
}

.stTextArea > div:nth-child(3) {
  display: none;
}

.st-ci {
	min-height: 200px;
}

.css-glyadz {
	font-size: 1rem;
}

.u-text {
  width: 100%;
  text-align: center;
  line-break: anywhere;
}

.u-section-1 {
  background-image: none;
}

.u-section-1 .u-image-1 {
  width: 925px;
  height: 507px;
  margin: 53px auto 0;
}

.u-section-1 .u-text-1 {
  font-size: 3.75rem;
  font-weight: 700;
  margin: 50px auto 0;
}

.u-section-1 .u-text-2 {
  font-size: 1.25rem;
  margin: 11px auto 0;
}

.u-section-1 .u-list-1 {
  margin-top: 50px;
  margin-bottom: 60px;
}

.u-section-1 .u-repeater-1 {
  grid-template-columns: 100%;
  grid-gap: 22px 22px;
}

.u-section-1 .u-list-item-1 {
  box-shadow: 5px 5px 20px 0 rgba(0,0,0,0.1);
  background-image: none;
}

.u-section-1 .u-container-layout-1 {
  padding: 30px 20px;
}

.u-section-1 .u-text-3 {
  margin-bottom: 0;
  margin-top: 0;
  font-size: 1.875rem;
}

@media (max-width: 1199px) {
  .u-section-1 .u-container-layout-1 {
    padding-left: 15px;
    padding-right: 15px;
  }
}

@media (max-width: 991px) {
  .u-section-1 .u-sheet-1 {
    min-height: 1396px;
  }

  .u-section-1 .u-image-1 {
    width: 720px;
    height: 394px;
  }

  .u-section-1 .u-text-1 {
    margin-top: 163px;
  }

  .u-section-1 .u-list-1 {
    margin-top: -63px;
  }
}

@media (max-width: 767px) {
  .u-section-1 .u-sheet-1 {
    min-height: 958px;
  }

  .u-section-1 .u-image-1 {
    width: 540px;
    height: 296px;
  }

  .u-section-1 .u-text-1 {
    margin-top: 261px;
  }

  .u-section-1 .u-list-1 {
    margin-top: -161px;
  }

  .u-section-1 .u-repeater-1 {
    grid-template-columns: calc(50% - 11px) calc(50% - 11px);
  }

  .u-section-1 .u-container-layout-1 {
    padding-left: 10px;
    padding-right: 10px;
  }
}

@media (max-width: 575px) {
  .u-section-1 .u-sheet-1 {
    min-height: 848px;
  }

  .u-section-1 .u-image-1 {
    width: 340px;
    height: 186px;
    margin-top: 58px;
  }

  .u-section-1 .u-text-1 {
    font-size: 2.25rem;
    margin-top: 366px;
  }

  .u-section-1 .u-text-2 {
    margin-left: 0;
    margin-right: 0;
  }

  .u-section-1 .u-list-1 {
    margin-top: -271px;
  }

  .u-section-1 .u-repeater-1 {
    grid-template-columns: 100%;
  }

  .u-section-1 .u-container-layout-1 {
    padding-left: 20px;
    padding-right: 20px;
  }
}

.u-section-2 .u-form-1 {
  height: 229px;
  margin: 0 0 60px;
}

@media (max-width: 1199px) {
  .u-section-2 .u-form-1 {
    margin-right: initial;
    margin-left: initial;
  }
} .u-section-3 {
  background-image: none;
}

.u-section-3 .u-sheet-1 {
  min-height: 590px;
}

.u-section-3 .u-text-1 {
  font-size: 3.75rem;
  font-weight: 700;
  margin: 70px auto 0;
}

.u-section-3 .u-text-2 {
  font-size: 1.25rem;
  margin: 11px auto 0;
}

.u-section-3 .u-list-1 {
  margin-top: 27px;
  margin-bottom: 54px;
}

.u-section-3 .u-repeater-1 {
  grid-template-columns: 100%;
  min-height: 330px;
  grid-gap: 22px 22px;
}

.u-section-3 .u-list-item-1 {
  box-shadow: 5px 5px 20px 0 rgba(0,0,0,0.1);
  background-image: none;
}

.u-section-3 .u-container-layout-1 {
  padding: 30px 20px;
}

.u-section-3 .u-text-3 {
  margin-bottom: 0;
  margin-top: 0;
  font-size: 1.875rem;
}

@media (max-width: 1199px) {
  .u-section-3 .u-container-layout-1 {
    padding-left: 15px;
    padding-right: 15px;
  }
}

@media (max-width: 991px) {
  .u-section-3 .u-sheet-1 {
    min-height: 1396px;
  }

  .u-section-3 .u-list-1 {
    margin-top: 477px;
  }

  .u-section-3 .u-repeater-1 {
    min-height: 597px;
  }
}

@media (max-width: 767px) {
  .u-section-3 .u-sheet-1 {
    min-height: 958px;
  }

  .u-section-3 .u-list-1 {
    margin-top: 379px;
  }

  .u-section-3 .u-repeater-1 {
    grid-template-columns: calc(50% - 11px) calc(50% - 11px);
  }

  .u-section-3 .u-container-layout-1 {
    padding-left: 10px;
    padding-right: 10px;
  }
}

@media (max-width: 575px) {
  .u-section-3 .u-sheet-1 {
    min-height: 848px;
  }

  .u-section-3 .u-text-1 {
    font-size: 2.25rem;
  }

  .u-section-3 .u-list-1 {
    margin-top: 269px;
  }

  .u-section-3 .u-repeater-1 {
    grid-template-columns: 100%;
  }

  .u-section-3 .u-container-layout-1 {
    padding-left: 20px;
    padding-right: 20px;
  }
}

.u-section-4 .u-form-1 {
  height: 229px;
  margin: 0 0 60px;
}

@media (max-width: 1199px) {
  .u-section-4 .u-form-1 {
    margin-right: initial;
    margin-left: initial;
  }
}
</style>
    """