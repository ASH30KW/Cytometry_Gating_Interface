<template>
  <div class="grid">
    <div class="main-card">
      <h1 :style="{ textAlign: 'left' }">Cytometry Gating Web Interface</h1>
      <div class="main-card margin-bottom-100 inline-block">
        <h2 :style="{ textAlign: 'left' }">General Information</h2>
        <Accordion :multiple="true">
          <AccordionTab header="Show more">
            <div class="grid">
              <div class="col">
                <div class="main-card">
                  <div>
                    <div class="grid">
                      <div class="col">
                        <div class="main-card">
                          <div id="BarChart"></div>
                        </div>
                        <div class="main-card">
                          <div id="PieChart"></div>
                        </div>
                      </div>
                      <div class="col">
                        <div class="main-card max-height: 100px">
                          <DataTable
                            :value="CellTypeInfo"
                            class="p-datatable"
                            responsiveLayout="scroll"
                          >
                            <Column field="title" header="Types"></Column>
                            <Column field="details" header="Number"></Column>
                          </DataTable>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </AccordionTab>
        </Accordion>
      </div>

      <div class="main-card margin-bottom-100 inline-block">
        <h2 :style="{ textAlign: 'left' }">Manual Gating</h2>
        <Accordion :multiple="true">
          <AccordionTab header="Show more">
            <div class="grid">
              <div class="col">
                <div class="main-card">
                  <TabView ref="tabview1">
                    <TabPanel header="1.Step">
                      <div>
                        <Toolbar class="toolbar">
                          <template #start>
                            Use lasso to select an area.
                          </template>
                        </Toolbar>
                        <Splitter>
                          <SplitterPanel>
                            <Splitter layout="horizontal">
                              <SplitterPanel :size="60">
                                <div class="col">
                                  <div class="main-card">
                                    <div id="ScatterPlot"></div>
                                    X Axis:
                                    <Dropdown
                                      class="axisdropdown"
                                      v-model="manualSelectedFeatureX1"
                                      :options="feature_selection"
                                      optionLabel="name"
                                      placeholder="Select a X Feature"
                                      @change="
                                        ScatterPlot(
                                          this.manualSelectedFeatureX1.code,
                                          this.manualSelectedFeatureY1.code
                                        )
                                      "
                                    />
                                    <div class="control-row">
                                      Y Axis:
                                      <Dropdown
                                        class="axisdropdown"
                                        v-model="manualSelectedFeatureY1"
                                        :options="feature_selection"
                                        optionLabel="name"
                                        placeholder="Select a X Feature"
                                        @change="
                                          ScatterPlot(
                                            this.manualSelectedFeatureX1.code,
                                            this.manualSelectedFeatureY1.code
                                          )
                                        "
                                      />
                                    </div>
                                  </div>
                                  <div class="main-card">
                                    <TabView ref="tabview1">
                                      <TabPanel header="PieChart">
                                        <div>
                                          <div class="grid">
                                            <div class="col">
                                              <div class="main-card">
                                                <div id="PieChart1"></div>
                                              </div>
                                            </div>
                                            <div class="col">
                                              <div
                                                class="main-card max-height: 100px"
                                              >
                                                <DataTable
                                                  :value="CellTypeInfo1"
                                                  class="p-datatable"
                                                  responsiveLayout="scroll"
                                                >
                                                  <Column
                                                    field="title"
                                                    header="Types"
                                                  ></Column>
                                                  <Column
                                                    field="details"
                                                    header="Percentiles to 1.Step"
                                                  ></Column>
                                                </DataTable>
                                              </div>
                                            </div>
                                          </div>
                                        </div>
                                      </TabPanel>
                                      <TabPanel header="BarChart">
                                        <div>
                                          <div class="grid">
                                            <div class="col">
                                              <div class="main-card">
                                                <div id="BarChart1"></div>
                                              </div>
                                            </div>
                                            <div class="col">
                                              <div
                                                class="main-card max-height: 100px"
                                              >
                                                <DataTable
                                                  :value="CellTypeInfo1"
                                                  class="p-datatable"
                                                  responsiveLayout="scroll"
                                                >
                                                  <Column
                                                    field="title"
                                                    header="Types"
                                                  ></Column>
                                                  <Column
                                                    field="details"
                                                    header="Percentiles to 1.Step"
                                                  ></Column>
                                                </DataTable>
                                              </div>
                                            </div>
                                          </div>
                                        </div>
                                      </TabPanel>
                                      <TabPanel header="BoxPlot">
                                        <div>
                                          <div class="grid">
                                            <div class="col">
                                              <div class="main-card">
                                                <div id="boxplot"></div>
                                              </div>
                                            </div>
                                            <div class="col">
                                              <div
                                                class="main-card max-height: 100px"
                                              >
                                                <DataTable
                                                  :value="CellTypeInfo1"
                                                  class="p-datatable"
                                                  responsiveLayout="scroll"
                                                >
                                                  <Column
                                                    field="title"
                                                    header="Types"
                                                  ></Column>
                                                  <Column
                                                    field="details"
                                                    header="Percentiles to 1.Step"
                                                  ></Column>
                                                </DataTable>
                                              </div>
                                            </div>
                                          </div>
                                        </div>
                                      </TabPanel>
                                      <TabPanel header="ViolinPlot">
                                        <div>
                                          <div class="grid">
                                            <div class="col">
                                              <div class="main-card">
                                                <div id="violin"></div>
                                              </div>
                                            </div>
                                            <div class="col">
                                              <div
                                                class="main-card max-height: 100px"
                                              >
                                                <DataTable
                                                  :value="CellTypeInfo1"
                                                  class="p-datatable"
                                                  responsiveLayout="scroll"
                                                >
                                                  <Column
                                                    field="title"
                                                    header="Types"
                                                  ></Column>
                                                  <Column
                                                    field="details"
                                                    header="Percentiles to 1.Step"
                                                  ></Column>
                                                </DataTable>
                                              </div>
                                            </div>
                                          </div>
                                        </div>
                                      </TabPanel>
                                    </TabView>
                                  </div>
                                </div>
                              </SplitterPanel>
                              <SplitterPanel :size="30">
                                <div class="main-card">
                                  <h4 :style="{ textAlign: 'mid' }">
                                    The first four images of each type were
                                    selected in the 1.Step using lasso.
                                  </h4>
                                </div>
                                <div class="main-card">
                                  <h5 :style="{ textAlign: 'mid' }">
                                    Lymphocytes
                                  </h5>
                                  <Carousel
                                    :value="LymImgs"
                                    :numVisible="3"
                                    :numScroll="2"
                                  >
                                    <template #item="slotProps">
                                      <div class="cell-item">
                                        <div class="image-wrapper-carousel">
                                          <img
                                            class="cell-image"
                                            :src="
                                              'data:image/png;base64,' +
                                              slotProps.data
                                            "
                                            alt="Valid cell"
                                          />
                                        </div>
                                      </div>
                                    </template>
                                  </Carousel>
                                </div>
                                <div class="main-card">
                                  <h5 :style="{ textAlign: 'mid' }">
                                    Monocytes
                                  </h5>
                                  <Carousel
                                    :value="MonImgs.slice(0, 8)"
                                    :numVisible="3"
                                    :numScroll="2"
                                  >
                                    <template #item="slotProps">
                                      <div class="cell-item">
                                        <div>
                                          <div class="image-wrapper-carousel">
                                            <img
                                              class="cell-image"
                                              :src="
                                                'data:image/png;base64,' +
                                                slotProps.data
                                              "
                                              alt="Valid cell"
                                            />
                                          </div>
                                        </div>
                                      </div>
                                    </template>
                                  </Carousel>
                                </div>
                                <div class="main-card">
                                  <h5 :style="{ textAlign: 'mid' }">
                                    Eosinophils
                                  </h5>
                                  <Carousel
                                    :value="EosImgs.slice(0, 8)"
                                    :numVisible="3"
                                    :numScroll="2"
                                  >
                                    <template #item="slotProps">
                                      <div class="cell-item">
                                        <div>
                                          <div class="image-wrapper-carousel">
                                            <img
                                              class="cell-image"
                                              :src="
                                                'data:image/png;base64,' +
                                                slotProps.data
                                              "
                                              alt="Valid cell"
                                            />
                                          </div>
                                        </div>
                                      </div>
                                    </template>
                                  </Carousel>
                                </div>
                                <div class="main-card">
                                  <h5 :style="{ textAlign: 'mid' }">
                                    Neutrophils
                                  </h5>
                                  <Carousel
                                    :value="NeuImgs.slice(0, 8)"
                                    :numVisible="3"
                                    :numScroll="2"
                                  >
                                    <template #item="slotProps">
                                      <div class="cell-item">
                                        <div>
                                          <div class="image-wrapper-carousel">
                                            <img
                                              class="cell-image"
                                              :src="
                                                'data:image/png;base64,' +
                                                slotProps.data
                                              "
                                              alt="Valid cell"
                                            />
                                          </div>
                                        </div>
                                      </div>
                                    </template>
                                  </Carousel>
                                </div>
                              </SplitterPanel>
                            </Splitter>
                          </SplitterPanel>
                        </Splitter>
                      </div>
                    </TabPanel>
                    <TabPanel header="2.Step">
                      <div>
                        <Toolbar class="toolbar">
                          <template #start>
                            After selecting the area in the 1.Step, click
                            Generate.
                            <Button
                              label="Generate"
                              @click="
                                this.ScatterPlot2(
                                  'dissimilarity',
                                  'correlation'
                                )
                              "
                              class="mr-1"
                            />
                          </template>
                        </Toolbar>
                        <Splitter v-show="Tab2Visible">
                          <SplitterPanel>
                            <Splitter layout="horizontal">
                              <SplitterPanel :size="60">
                                <div class="col">
                                  <div class="bubbleplot" data-num="2">
                                    <div class="main-card">
                                      <div id="ScatterPlot2"></div>
                                      X Axis:
                                      <Dropdown
                                        class="axisdropdown"
                                        v-model="manualSelectedFeatureX2"
                                        :options="feature_selection"
                                        optionLabel="name"
                                        placeholder="Select a X Feature"
                                        @change="
                                          ScatterPlot2(
                                            this.manualSelectedFeatureX2.code,
                                            this.manualSelectedFeatureY2.code
                                          )
                                        "
                                      />
                                      <div class="control-row">
                                        Y Axis:
                                        <Dropdown
                                          class="axisdropdown"
                                          v-model="manualSelectedFeatureY2"
                                          :options="feature_selection"
                                          optionLabel="name"
                                          placeholder="Select a X Feature"
                                          @change="
                                            ScatterPlot2(
                                              this.manualSelectedFeatureX2.code,
                                              this.manualSelectedFeatureY2.code
                                            )
                                          "
                                        />
                                      </div>
                                    </div>
                                  </div>
                                  <div class="main-card">
                                    <TabView ref="tabview1">
                                      <TabPanel header="PieChart">
                                        <div>
                                          <div class="grid">
                                            <div class="col">
                                              <div class="main-card">
                                                <div id="PieChart2"></div>
                                              </div>
                                            </div>
                                            <div class="col">
                                              <div
                                                class="main-card max-height: 100px"
                                              >
                                                <DataTable
                                                  :value="CellTypeInfo2"
                                                  class="p-datatable"
                                                  responsiveLayout="scroll"
                                                >
                                                  <Column
                                                    field="title"
                                                    header="Types"
                                                  ></Column>
                                                  <Column
                                                    field="details"
                                                    header="Percentiles to 1.Step"
                                                  ></Column>
                                                </DataTable>
                                              </div>
                                            </div>
                                          </div>
                                        </div>
                                      </TabPanel>
                                      <TabPanel header="BarChart">
                                        <div>
                                          <div class="grid">
                                            <div class="col">
                                              <div class="main-card">
                                                <div id="BarChart2"></div>
                                              </div>
                                            </div>
                                            <div class="col">
                                              <div
                                                class="main-card max-height: 100px"
                                              >
                                                <DataTable
                                                  :value="CellTypeInfo2"
                                                  class="p-datatable"
                                                  responsiveLayout="scroll"
                                                >
                                                  <Column
                                                    field="title"
                                                    header="Types"
                                                  ></Column>
                                                  <Column
                                                    field="details"
                                                    header="Percentiles to 1.Step"
                                                  ></Column>
                                                </DataTable>
                                              </div>
                                            </div>
                                          </div>
                                        </div>
                                      </TabPanel>
                                      <TabPanel header="BoxPlot">
                                        <div>
                                          <div class="grid">
                                            <div class="col">
                                              <div class="main-card">
                                                <div id="BoxPlot2"></div>
                                              </div>
                                            </div>
                                            <div class="col">
                                              <div
                                                class="main-card max-height: 100px"
                                              >
                                                <DataTable
                                                  :value="CellTypeInfo2"
                                                  class="p-datatable"
                                                  responsiveLayout="scroll"
                                                >
                                                  <Column
                                                    field="title"
                                                    header="Types"
                                                  ></Column>
                                                  <Column
                                                    field="details"
                                                    header="Percentiles to 1.Step"
                                                  ></Column>
                                                </DataTable>
                                              </div>
                                            </div>
                                          </div>
                                        </div>
                                      </TabPanel>
                                      <TabPanel header="ViolinPlot">
                                        <div>
                                          <div class="grid">
                                            <div class="col">
                                              <div class="main-card">
                                                <div id="Violin2"></div>
                                              </div>
                                            </div>
                                            <div class="col">
                                              <div
                                                class="main-card max-height: 100px"
                                              >
                                                <DataTable
                                                  :value="CellTypeInfo2"
                                                  class="p-datatable"
                                                  responsiveLayout="scroll"
                                                >
                                                  <Column
                                                    field="title"
                                                    header="Types"
                                                  ></Column>
                                                  <Column
                                                    field="details"
                                                    header="Percentiles to 1.Step"
                                                  ></Column>
                                                </DataTable>
                                              </div>
                                            </div>
                                          </div>
                                        </div>
                                      </TabPanel>
                                    </TabView>
                                  </div>
                                </div>
                              </SplitterPanel>
                              <SplitterPanel :size="30">
                                <div class="main-card">
                                  <h4 :style="{ textAlign: 'mid' }">
                                    The first four images of each type were
                                    selected in the 2.Step using lasso.
                                  </h4>
                                </div>
                                <div class="main-card">
                                  <h5 :style="{ textAlign: 'mid' }">
                                    Lymphocytes
                                  </h5>
                                  <Carousel
                                    :value="LymImgs.slice(0, 8)"
                                    :numVisible="3"
                                    :numScroll="2"
                                  >
                                    <template #item="slotProps">
                                      <div class="cell-item">
                                        <div>
                                          <div class="image-wrapper-carousel">
                                            <img
                                              class="cell-image"
                                              :src="
                                                'data:image/png;base64,' +
                                                slotProps.data
                                              "
                                              alt="Valid cell"
                                            />
                                          </div>
                                        </div>
                                      </div>
                                    </template>
                                  </Carousel>
                                </div>
                                <div class="main-card">
                                  <h5 :style="{ textAlign: 'mid' }">
                                    Monocytes
                                  </h5>
                                  <Carousel
                                    :value="MonImgs.slice(0, 8)"
                                    :numVisible="3"
                                    :numScroll="2"
                                  >
                                    <template #item="slotProps">
                                      <div class="cell-item">
                                        <div>
                                          <div class="image-wrapper-carousel">
                                            <img
                                              class="cell-image"
                                              :src="
                                                'data:image/png;base64,' +
                                                slotProps.data
                                              "
                                              alt="Valid cell"
                                            />
                                          </div>
                                        </div>
                                      </div>
                                    </template>
                                  </Carousel>
                                </div>
                                <div class="main-card">
                                  <h5 :style="{ textAlign: 'mid' }">
                                    Eosinophils
                                  </h5>
                                  <Carousel
                                    :value="EosImgs.slice(0, 8)"
                                    :numVisible="3"
                                    :numScroll="2"
                                  >
                                    <template #item="slotProps">
                                      <div class="cell-item">
                                        <div>
                                          <div class="image-wrapper-carousel">
                                            <!-- <div>{{ slotProps.data.label}}</div> -->
                                            <img
                                              class="cell-image"
                                              :src="
                                                'data:image/png;base64,' +
                                                slotProps.data
                                              "
                                              alt="Valid cell"
                                            />
                                          </div>
                                        </div>
                                      </div>
                                    </template>
                                  </Carousel>
                                </div>
                                <div class="main-card">
                                  <h5 :style="{ textAlign: 'mid' }">
                                    Neutrophils
                                  </h5>
                                  <Carousel
                                    :value="NeuImgs.slice(0, 8)"
                                    :numVisible="3"
                                    :numScroll="2"
                                  >
                                    <template #item="slotProps">
                                      <div class="cell-item">
                                        <div>
                                          <div class="image-wrapper-carousel">
                                            <img
                                              class="cell-image"
                                              :src="
                                                'data:image/png;base64,' +
                                                slotProps.data
                                              "
                                              alt="Valid cell"
                                            />
                                          </div>
                                        </div>
                                      </div>
                                    </template>
                                  </Carousel>
                                </div>
                              </SplitterPanel>
                            </Splitter>
                          </SplitterPanel>
                        </Splitter>
                      </div>
                    </TabPanel>
                    <TabPanel header="3.Step">
                      <div>
                        <Toolbar class="toolbar">
                          <template #start>
                            After selecting the area in the 2.Step, click
                            Generate.
                            <Button
                              label="Generate"
                              @click="
                                this.ScatterPlot3(
                                  'dissimilarity',
                                  'correlation'
                                )
                              "
                              class="mr-2"
                            />
                          </template>
                        </Toolbar>
                        <Splitter>
                          <SplitterPanel v-show="Tab3Visible">
                            <Splitter layout="horizontal">
                              <SplitterPanel :size="60">
                                <div class="col">
                                  <div class="bubbleplot" data-num="3">
                                    <div class="main-card">
                                      <div id="ScatterPlot3"></div>
                                      X Axis:
                                      <Dropdown
                                        class="axisdropdown"
                                        v-model="manualSelectedFeatureX3"
                                        :options="feature_selection"
                                        optionLabel="name"
                                        placeholder="Select a X Feature"
                                        @change="
                                          ScatterPlot3(
                                            this.manualSelectedFeatureX3.code,
                                            this.manualSelectedFeatureY3.code
                                          )
                                        "
                                      />
                                      <div class="control-row">
                                        Y Axis:
                                        <Dropdown
                                          class="axisdropdown"
                                          v-model="manualSelectedFeatureY3"
                                          :options="feature_selection"
                                          optionLabel="name"
                                          placeholder="Select a X Feature"
                                          @change="
                                            ScatterPlot3(
                                              this.manualSelectedFeatureX3.code,
                                              this.manualSelectedFeatureY3.code
                                            )
                                          "
                                        />
                                      </div>
                                    </div>
                                  </div>
                                  <div class="main-card">
                                    <TabView ref="tabview1">
                                      <TabPanel header="PieChart">
                                        <div>
                                          <div class="grid">
                                            <div class="col">
                                              <div class="main-card">
                                                <div id="PieChart3"></div>
                                              </div>
                                            </div>
                                            <div class="col">
                                              <div
                                                class="main-card max-height: 100px"
                                              >
                                                <DataTable
                                                  :value="CellTypeInfo3"
                                                  class="p-datatable"
                                                  responsiveLayout="scroll"
                                                >
                                                  <Column
                                                    field="title"
                                                    header="Types"
                                                  ></Column>
                                                  <Column
                                                    field="details"
                                                    header="Percentiles to 1.Step"
                                                  ></Column>
                                                </DataTable>
                                              </div>
                                            </div>
                                          </div>
                                        </div>
                                      </TabPanel>
                                      <TabPanel header="BarChart">
                                        <div>
                                          <div class="grid">
                                            <div class="col">
                                              <div class="main-card">
                                                <div id="BarChart3"></div>
                                              </div>
                                            </div>
                                            <div class="col">
                                              <div
                                                class="main-card max-height: 100px"
                                              >
                                                <DataTable
                                                  :value="CellTypeInfo3"
                                                  class="p-datatable"
                                                  responsiveLayout="scroll"
                                                >
                                                  <Column
                                                    field="title"
                                                    header="Types"
                                                  ></Column>
                                                  <Column
                                                    field="details"
                                                    header="Percentiles to 1.Step"
                                                  ></Column>
                                                </DataTable>
                                              </div>
                                            </div>
                                          </div>
                                        </div>
                                      </TabPanel>
                                      <TabPanel header="BoxPlot">
                                        <div>
                                          <div class="grid">
                                            <div class="col">
                                              <div class="main-card">
                                                <div id="BoxPlot3"></div>
                                              </div>
                                            </div>
                                            <div class="col">
                                              <div
                                                class="main-card max-height: 100px"
                                              >
                                                <DataTable
                                                  :value="CellTypeInfo3"
                                                  class="p-datatable"
                                                  responsiveLayout="scroll"
                                                >
                                                  <Column
                                                    field="title"
                                                    header="Types"
                                                  ></Column>
                                                  <Column
                                                    field="details"
                                                    header="Percentiles to 1.Step"
                                                  ></Column>
                                                </DataTable>
                                              </div>
                                            </div>
                                          </div>
                                        </div>
                                      </TabPanel>
                                      <TabPanel header="ViolinPlot">
                                        <div>
                                          <div class="grid">
                                            <div class="col">
                                              <div class="main-card">
                                                <div id="Violin3"></div>
                                              </div>
                                            </div>
                                            <div class="col">
                                              <div
                                                class="main-card max-height: 100px"
                                              >
                                                <DataTable
                                                  :value="CellTypeInfo3"
                                                  class="p-datatable"
                                                  responsiveLayout="scroll"
                                                >
                                                  <Column
                                                    field="title"
                                                    header="Types"
                                                  ></Column>
                                                  <Column
                                                    field="details"
                                                    header="Percentiles to 1.Step"
                                                  ></Column>
                                                </DataTable>
                                              </div>
                                            </div>
                                          </div>
                                        </div>
                                      </TabPanel>
                                    </TabView>
                                  </div>
                                </div>
                              </SplitterPanel>
                              <SplitterPanel :size="30">
                                <div class="main-card">
                                  <h4 :style="{ textAlign: 'mid' }">
                                    The first four images of each type were
                                    selected in the 3.Step using lasso.
                                  </h4>
                                </div>
                                <div class="main-card">
                                  <h5 :style="{ textAlign: 'mid' }">
                                    Lymphocytes
                                  </h5>
                                  <Carousel
                                    :value="LymImgs.slice(0, 8)"
                                    :numVisible="3"
                                    :numScroll="2"
                                  >
                                    <template #item="slotProps">
                                      <div class="cell-item">
                                        <div>
                                          <div class="image-wrapper-carousel">
                                            <img
                                              class="cell-image"
                                              :src="
                                                'data:image/png;base64,' +
                                                slotProps.data
                                              "
                                              alt="Valid cell"
                                            />
                                          </div>
                                        </div>
                                      </div>
                                    </template>
                                  </Carousel>
                                </div>
                                <div class="main-card">
                                  <h5 :style="{ textAlign: 'mid' }">
                                    Monocytes
                                  </h5>
                                  <Carousel
                                    :value="MonImgs.slice(0, 8)"
                                    :numVisible="3"
                                    :numScroll="2"
                                  >
                                    <template #item="slotProps">
                                      <div class="cell-item">
                                        <div>
                                          <div class="image-wrapper-carousel">
                                            <img
                                              class="cell-image"
                                              :src="
                                                'data:image/png;base64,' +
                                                slotProps.data
                                              "
                                              alt="Valid cell"
                                            />
                                          </div>
                                        </div>
                                      </div>
                                    </template>
                                  </Carousel>
                                </div>
                                <div class="main-card">
                                  <h5 :style="{ textAlign: 'mid' }">
                                    Eosinophils
                                  </h5>
                                  <Carousel
                                    :value="EosImgs.slice(0, 8)"
                                    :numVisible="3"
                                    :numScroll="2"
                                  >
                                    <template #item="slotProps">
                                      <div class="cell-item">
                                        <div>
                                          <div class="image-wrapper-carousel">
                                            <img
                                              class="cell-image"
                                              :src="
                                                'data:image/png;base64,' +
                                                slotProps.data
                                              "
                                              alt="Valid cell"
                                            />
                                          </div>
                                        </div>
                                      </div>
                                    </template>
                                  </Carousel>
                                </div>
                                <div class="main-card">
                                  <h5 :style="{ textAlign: 'mid' }">
                                    Neutrophils
                                  </h5>
                                  <Carousel
                                    :value="NeuImgs.slice(0, 8)"
                                    :numVisible="3"
                                    :numScroll="2"
                                  >
                                    <template #item="slotProps">
                                      <div class="cell-item">
                                        <div>
                                          <div class="image-wrapper-carousel">
                                            <img
                                              class="cell-image"
                                              :src="
                                                'data:image/png;base64,' +
                                                slotProps.data
                                              "
                                              alt="Valid cell"
                                            />
                                          </div>
                                        </div>
                                      </div>
                                    </template>
                                  </Carousel>
                                </div>
                              </SplitterPanel>
                            </Splitter>
                          </SplitterPanel>
                        </Splitter>
                      </div>
                    </TabPanel>
                    <TabPanel header="4.Step">
                      <div>
                        <Toolbar class="toolbar">
                          <template #start>
                            After selecting the area in the 3.Step, click
                            Generate.
                            <Button
                              label="Generate"
                              @click="
                                this.ScatterPlot4(
                                  'dissimilarity',
                                  'correlation'
                                )
                              "
                              class="mr-2"
                            />
                          </template>
                        </Toolbar>
                        <Splitter v-show="Tab4Visible">
                          <SplitterPanel>
                            <Splitter layout="horizontal">
                              <SplitterPanel :size="60">
                                <div class="col">
                                  <div class="bubbleplot" data-num="4">
                                    <div class="main-card">
                                      <div id="ScatterPlot4"></div>
                                      X Axis:
                                      <Dropdown
                                        class="axisdropdown"
                                        v-model="manualSelectedFeatureX4"
                                        :options="feature_selection"
                                        optionLabel="name"
                                        placeholder="Select a X Feature"
                                        @change="
                                          ScatterPlot4(
                                            this.manualSelectedFeatureX4.code,
                                            this.manualSelectedFeatureY4.code
                                          )
                                        "
                                      />
                                      <div class="control-row">
                                        Y Axis:
                                        <Dropdown
                                          class="axisdropdown"
                                          v-model="manualSelectedFeatureY4"
                                          :options="feature_selection"
                                          optionLabel="name"
                                          placeholder="Select a X Feature"
                                          @change="
                                            ScatterPlot4(
                                              this.manualSelectedFeatureX4.code,
                                              this.manualSelectedFeatureY4.code
                                            )
                                          "
                                        />
                                      </div>
                                    </div>
                                  </div>
                                  <div class="main-card">
                                    <TabView ref="tabview1">
                                      <TabPanel header="PieChart">
                                        <div>
                                          <div class="grid">
                                            <div class="col">
                                              <div class="main-card">
                                                <div id="PieChart4"></div>
                                              </div>
                                            </div>
                                            <div class="col">
                                              <div
                                                class="main-card max-height: 100px"
                                              >
                                                <DataTable
                                                  :value="CellTypeInfo4"
                                                  class="p-datatable"
                                                  responsiveLayout="scroll"
                                                >
                                                  <Column
                                                    field="title"
                                                    header="Types"
                                                  ></Column>
                                                  <Column
                                                    field="details"
                                                    header="Percentiles to 1.Step"
                                                  ></Column>
                                                </DataTable>
                                              </div>
                                            </div>
                                          </div>
                                        </div>
                                      </TabPanel>
                                      <TabPanel header="BarChart">
                                        <div>
                                          <div class="grid">
                                            <div class="col">
                                              <div class="main-card">
                                                <div id="BarChart4"></div>
                                              </div>
                                            </div>
                                            <div class="col">
                                              <div
                                                class="main-card max-height: 100px"
                                              >
                                                <DataTable
                                                  :value="CellTypeInfo4"
                                                  class="p-datatable"
                                                  responsiveLayout="scroll"
                                                >
                                                  <Column
                                                    field="title"
                                                    header="Types"
                                                  ></Column>
                                                  <Column
                                                    field="details"
                                                    header="Percentiles to 1.Step"
                                                  ></Column>
                                                </DataTable>
                                              </div>
                                            </div>
                                          </div>
                                        </div>
                                      </TabPanel>
                                      <TabPanel header="BoxPlot">
                                        <div>
                                          <div class="grid">
                                            <div class="col">
                                              <div class="main-card">
                                                <div id="BoxPlot4"></div>
                                              </div>
                                            </div>
                                            <div class="col">
                                              <div
                                                class="main-card max-height: 100px"
                                              >
                                                <DataTable
                                                  :value="CellTypeInfo4"
                                                  class="p-datatable"
                                                  responsiveLayout="scroll"
                                                >
                                                  <Column
                                                    field="title"
                                                    header="Types"
                                                  ></Column>
                                                  <Column
                                                    field="details"
                                                    header="Percentiles to 1.Step"
                                                  ></Column>
                                                </DataTable>
                                              </div>
                                            </div>
                                          </div>
                                        </div>
                                      </TabPanel>
                                      <TabPanel header="ViolinPlot">
                                        <div>
                                          <div class="grid">
                                            <div class="col">
                                              <div class="main-card">
                                                <div id="Violin4"></div>
                                              </div>
                                            </div>
                                            <div class="col">
                                              <div
                                                class="main-card max-height: 100px"
                                              >
                                                <DataTable
                                                  :value="CellTypeInfo4"
                                                  class="p-datatable"
                                                  responsiveLayout="scroll"
                                                >
                                                  <Column
                                                    field="title"
                                                    header="Types"
                                                  ></Column>
                                                  <Column
                                                    field="details"
                                                    header="Percentiles to 1.Step"
                                                  ></Column>
                                                </DataTable>
                                              </div>
                                            </div>
                                          </div>
                                        </div>
                                      </TabPanel>
                                    </TabView>
                                  </div>
                                </div>
                              </SplitterPanel>
                              <SplitterPanel :size="30">
                                <div class="main-card">
                                  <h4 :style="{ textAlign: 'mid' }">
                                    The first four images of each type were
                                    selected in the 4.Step using lasso.
                                  </h4>
                                </div>
                                <div class="main-card">
                                  <h5 :style="{ textAlign: 'mid' }">
                                    Lymphocytes
                                  </h5>
                                  <Carousel
                                    :value="LymImgs"
                                    :numVisible="3"
                                    :numScroll="2"
                                  >
                                    <template #item="slotProps">
                                      <div class="cell-item">
                                        <div>
                                          <div class="image-wrapper-carousel">
                                            <img
                                              class="cell-image"
                                              :src="
                                                'data:image/png;base64,' +
                                                slotProps.data
                                              "
                                              alt="Valid cell"
                                            />
                                          </div>
                                        </div>
                                      </div>
                                    </template>
                                  </Carousel>
                                </div>
                                <div class="main-card">
                                  <h5 :style="{ textAlign: 'mid' }">
                                    Monocytes
                                  </h5>
                                  <Carousel
                                    :value="MonImgs"
                                    :numVisible="3"
                                    :numScroll="2"
                                  >
                                    <template #item="slotProps">
                                      <div class="cell-item">
                                        <div>
                                          <div class="image-wrapper-carousel">
                                            <img
                                              class="cell-image"
                                              :src="
                                                'data:image/png;base64,' +
                                                slotProps.data
                                              "
                                              alt="Valid cell"
                                            />
                                          </div>
                                        </div>
                                      </div>
                                    </template>
                                  </Carousel>
                                </div>
                                <div class="main-card">
                                  <h5 :style="{ textAlign: 'mid' }">
                                    Eosinophils
                                  </h5>
                                  <Carousel
                                    :value="EosImgs"
                                    :numVisible="3"
                                    :numScroll="2"
                                  >
                                    <template #item="slotProps">
                                      <div class="cell-item">
                                        <div>
                                          <div class="image-wrapper-carousel">
                                            <img
                                              class="cell-image"
                                              :src="
                                                'data:image/png;base64,' +
                                                slotProps.data
                                              "
                                              alt="Valid cell"
                                            />
                                          </div>
                                        </div>
                                      </div>
                                    </template>
                                  </Carousel>
                                </div>
                                <div class="main-card">
                                  <h5 :style="{ textAlign: 'mid' }">
                                    Neutrophils
                                  </h5>
                                  <Carousel
                                    :value="NeuImgs"
                                    :numVisible="3"
                                    :numScroll="2"
                                  >
                                    <template #item="slotProps">
                                      <div class="cell-item">
                                        <div>
                                          <div class="image-wrapper-carousel">
                                            <img
                                              class="cell-image"
                                              :src="
                                                'data:image/png;base64,' +
                                                slotProps.data
                                              "
                                              alt="Valid cell"
                                            />
                                          </div>
                                        </div>
                                      </div>
                                    </template>
                                  </Carousel>
                                </div>
                              </SplitterPanel>
                            </Splitter>
                          </SplitterPanel>
                        </Splitter>
                      </div>
                    </TabPanel>
                    <TabPanel header="5.Step">
                      <div>
                        <Toolbar class="toolbar">
                          <template #start>
                            After selecting the area in the 4.Step, click
                            Generate.
                            <Button
                              label="Generate"
                              @click="
                                this.ScatterPlot5(
                                  'dissimilarity',
                                  'correlation'
                                )
                              "
                              class="mr-2"
                            />
                          </template>
                        </Toolbar>
                        <Splitter v-show="Tab5Visible">
                          <SplitterPanel>
                            <Splitter layout="horizontal">
                              <SplitterPanel :size="60">
                                <div class="col">
                                  <div class="bubbleplot" data-num="5">
                                    <div class="main-card">
                                      <div id="ScatterPlot5"></div>
                                      X Axis:
                                      <Dropdown
                                        class="axisdropdown"
                                        v-model="manualSelectedFeatureX5"
                                        :options="feature_selection"
                                        optionLabel="name"
                                        placeholder="Select a X Feature"
                                        @change="
                                          ScatterPlot5(
                                            this.manualSelectedFeatureX5.code,
                                            this.manualSelectedFeatureY5.code
                                          )
                                        "
                                      />
                                      <div class="control-row">
                                        Y Axis:
                                        <Dropdown
                                          class="axisdropdown"
                                          v-model="manualSelectedFeatureY5"
                                          :options="feature_selection"
                                          optionLabel="name"
                                          placeholder="Select a X Feature"
                                          @change="
                                            ScatterPlot5(
                                              this.manualSelectedFeatureX5.code,
                                              this.manualSelectedFeatureY5.code
                                            )
                                          "
                                        />
                                      </div>
                                    </div>
                                  </div>
                                  <div class="main-card">
                                    <TabView ref="tabview1">
                                      <TabPanel header="PieChart">
                                        <div>
                                          <div class="grid">
                                            <div class="col">
                                              <div class="main-card">
                                                <div id="PieChart5"></div>
                                              </div>
                                            </div>
                                            <div class="col">
                                              <div
                                                class="main-card max-height: 100px"
                                              >
                                                <DataTable
                                                  :value="CellTypeInfo5"
                                                  class="p-datatable"
                                                  responsiveLayout="scroll"
                                                >
                                                  <Column
                                                    field="title"
                                                    header="Types"
                                                  ></Column>
                                                  <Column
                                                    field="details"
                                                    header="Percentiles to 1.Step"
                                                  ></Column>
                                                </DataTable>
                                              </div>
                                            </div>
                                          </div>
                                        </div>
                                      </TabPanel>
                                      <TabPanel header="BarChart">
                                        <div>
                                          <div class="grid">
                                            <div class="col">
                                              <div class="main-card">
                                                <div id="BarChart5"></div>
                                              </div>
                                            </div>
                                            <div class="col">
                                              <div
                                                class="main-card max-height: 100px"
                                              >
                                                <DataTable
                                                  :value="CellTypeInfo5"
                                                  class="p-datatable"
                                                  responsiveLayout="scroll"
                                                >
                                                  <Column
                                                    field="title"
                                                    header="Types"
                                                  ></Column>
                                                  <Column
                                                    field="details"
                                                    header="Percentiles to 1.Step"
                                                  ></Column>
                                                </DataTable>
                                              </div>
                                            </div>
                                          </div>
                                        </div>
                                      </TabPanel>
                                      <TabPanel header="BoxPlot">
                                        <div>
                                          <div class="grid">
                                            <div class="col">
                                              <div class="main-card">
                                                <div id="BoxPlot5"></div>
                                              </div>
                                            </div>
                                            <div class="col">
                                              <div
                                                class="main-card max-height: 100px"
                                              >
                                                <DataTable
                                                  :value="CellTypeInfo5"
                                                  class="p-datatable"
                                                  responsiveLayout="scroll"
                                                >
                                                  <Column
                                                    field="title"
                                                    header="Types"
                                                  ></Column>
                                                  <Column
                                                    field="details"
                                                    header="Percentiles to 1.Step"
                                                  ></Column>
                                                </DataTable>
                                              </div>
                                            </div>
                                          </div>
                                        </div>
                                      </TabPanel>
                                      <TabPanel header="ViolinPlot">
                                        <div>
                                          <div class="grid">
                                            <div class="col">
                                              <div class="main-card">
                                                <div id="Violin5"></div>
                                              </div>
                                            </div>
                                            <div class="col">
                                              <div
                                                class="main-card max-height: 100px"
                                              >
                                                <DataTable
                                                  :value="CellTypeInfo5"
                                                  class="p-datatable"
                                                  responsiveLayout="scroll"
                                                >
                                                  <Column
                                                    field="title"
                                                    header="Types"
                                                  ></Column>
                                                  <Column
                                                    field="details"
                                                    header="Percentiles to 1.Step"
                                                  ></Column>
                                                </DataTable>
                                              </div>
                                            </div>
                                          </div>
                                        </div>
                                      </TabPanel>
                                    </TabView>
                                  </div>
                                </div>
                              </SplitterPanel>
                              <SplitterPanel :size="30">
                                <div class="main-card">
                                  <h4 :style="{ textAlign: 'mid' }">
                                    The first four images of each type were
                                    selected in the 3.Step using lasso.
                                  </h4>
                                </div>
                                <div class="main-card">
                                  <h5 :style="{ textAlign: 'mid' }">
                                    Lymphocytes
                                  </h5>
                                  <Carousel
                                    :value="LymImgs"
                                    :numVisible="3"
                                    :numScroll="2"
                                  >
                                    <template #item="slotProps">
                                      <div class="cell-item">
                                        <div>
                                          <div class="image-wrapper-carousel">
                                            <img
                                              class="cell-image"
                                              :src="
                                                'data:image/png;base64,' +
                                                slotProps.data
                                              "
                                              alt="Valid cell"
                                            />
                                          </div>
                                        </div>
                                      </div>
                                    </template>
                                  </Carousel>
                                </div>
                                <div class="main-card">
                                  <h5 :style="{ textAlign: 'mid' }">
                                    Monocytes
                                  </h5>
                                  <Carousel
                                    :value="MonImgs.slice(0, 8)"
                                    :numVisible="3"
                                    :numScroll="2"
                                  >
                                    <template #item="slotProps">
                                      <div class="cell-item">
                                        <div>
                                          <div class="image-wrapper-carousel">
                                            <img
                                              class="cell-image"
                                              :src="
                                                'data:image/png;base64,' +
                                                slotProps.data
                                              "
                                              alt="Valid cell"
                                            />
                                          </div>
                                        </div>
                                      </div>
                                    </template>
                                  </Carousel>
                                </div>
                                <div class="main-card">
                                  <h5 :style="{ textAlign: 'mid' }">
                                    Eosinophils
                                  </h5>
                                  <Carousel
                                    :value="EosImgs.slice(0, 8)"
                                    :numVisible="3"
                                    :numScroll="2"
                                  >
                                    <template #item="slotProps">
                                      <div class="cell-item">
                                        <div>
                                          <div class="image-wrapper-carousel">
                                            <img
                                              class="cell-image"
                                              :src="
                                                'data:image/png;base64,' +
                                                slotProps.data
                                              "
                                              alt="Valid cell"
                                            />
                                          </div>
                                        </div>
                                      </div>
                                    </template>
                                  </Carousel>
                                </div>
                                <div class="main-card">
                                  <h5 :style="{ textAlign: 'mid' }">
                                    Neutrophils
                                  </h5>
                                  <Carousel
                                    :value="NeuImgs.slice(0, 8)"
                                    :numVisible="3"
                                    :numScroll="2"
                                  >
                                    <template #item="slotProps">
                                      <div class="cell-item">
                                        <div>
                                          <div class="image-wrapper-carousel">
                                            <img
                                              class="cell-image"
                                              :src="
                                                'data:image/png;base64,' +
                                                slotProps.data
                                              "
                                              alt="Valid cell"
                                            />
                                          </div>
                                        </div>
                                      </div>
                                    </template>
                                  </Carousel>
                                </div>
                              </SplitterPanel>
                            </Splitter>
                          </SplitterPanel>
                        </Splitter>
                      </div>
                    </TabPanel>
                  </TabView>
                </div>
              </div>
            </div>
            <Dialog v-model:visible="particularScatterCellVisible">
              <div>
                <img
                  class="cell-image"
                  :src="'data:image/png;base64,' + ClickImg"
                  alt="Valid cell"
                />
              </div>
            </Dialog>
          </AccordionTab>
        </Accordion>
      </div>

      <div class="main-card margin-bottom-100 inline-block">
        <h2 :style="{ textAlign: 'left' }">
          Machine Learning supported Gating
        </h2>
        <Accordion :multiple="true">
          <AccordionTab header="Show more">
            <div class="grid p-fluid">
              <div class="p-inputgroup"></div>
            </div>
            <h3 :style="{ textAlign: 'left' }">
              Machine Learning supported Gating
            </h3>
            <Splitter layout="horizontal">
              <SplitterPanel :size="60">
                <div class="col">
                  <div class="bubbleplot" data-num="1">
                    <div class="main-card">
                      <div id="AICluster"></div>
                      <div class="control-row">
                        Algorithm:
                        <Dropdown
                          class="algodropdown"
                          v-model="selectedAlgo"
                          :options="clusterAlgo"
                          optionLabel="name"
                          placeholder="Select a X Feature"
                          @change="
                            Cluster(
                              this.selectedAlgo.code,
                              this.aiSelectedFeatureX.code,
                              this.aiSelectedFeatureY.code
                            )
                          "
                        />
                      </div>

                      X Axis:
                      <Dropdown
                        class="axisdropdown"
                        v-model="aiSelectedFeatureX"
                        :options="feature_selection"
                        optionLabel="name"
                        placeholder="Select a X Feature"
                        @change="
                          Cluster(
                            this.selectedAlgo.code,
                            this.aiSelectedFeatureX.code,
                            this.aiSelectedFeatureY.code
                          )
                        "
                      />
                      <div class="control-row">
                        Y Axis:
                        <Dropdown
                          class="axisdropdown"
                          v-model="aiSelectedFeatureY"
                          :options="feature_selection"
                          optionLabel="name"
                          placeholder="Select a X Feature"
                          @change="
                            Cluster(
                              this.selectedAlgo.code,
                              this.aiSelectedFeatureX.code,
                              this.aiSelectedFeatureY.code
                            )
                          "
                        />
                      </div>
                    </div>
                  </div>
                  <div class="main-card">
                    <TabView ref="tabview1">
                      <TabPanel header="PieChart">
                        <div>
                          <div class="grid">
                            <div class="col">
                              <div class="main-card">
                                <div id="PieChartAI"></div>
                              </div>
                            </div>
                            <div class="col">
                              <div class="main-card max-height: 100px">
                                <DataTable
                                  :value="EvaluationData"
                                  class="p-datatable"
                                  responsiveLayout="scroll"
                                >
                                  <Column
                                    field="title"
                                    header="Evaluation"
                                  ></Column>
                                  <Column
                                    field="details"
                                    header="Details"
                                  ></Column>
                                </DataTable>
                              </div>
                            </div>
                          </div>
                        </div>
                      </TabPanel>
                      <TabPanel header="BarChart">
                        <div>
                          <div class="grid">
                            <div class="col">
                              <div class="main-card">
                                <div id="BarChartAI"></div>
                              </div>
                            </div>
                            <div class="col">
                              <div class="main-card max-height: 100px">
                                <DataTable
                                  :value="EvaluationData"
                                  class="p-datatable"
                                  responsiveLayout="scroll"
                                >
                                  <Column
                                    field="title"
                                    header="Evaluation"
                                  ></Column>
                                  <Column
                                    field="details"
                                    header="Details"
                                  ></Column>
                                </DataTable>
                              </div>
                            </div>
                          </div>
                        </div>
                      </TabPanel>
                    </TabView>
                  </div>
                </div>
              </SplitterPanel>
              <SplitterPanel :size="30">
                <div class="main-card">
                  <h4 :style="{ textAlign: 'mid' }">
                    The first four images of each cluster were selected in AI
                    Gating using lasso.
                  </h4>
                </div>
                <div class="main-card">
                  <h5 :style="{ textAlign: 'mid' }">Cluster0</h5>
                  <Carousel :value="cluster0" :numVisible="3" :numScroll="2">
                    <template #item="slotProps">
                      <div class="cell-item">
                        <div>
                          <div class="image-wrapper-carousel">
                            <img
                              class="cell-image"
                              :src="'data:image/png;base64,' + slotProps.data"
                              alt="Valid cell"
                            />
                          </div>
                        </div>
                      </div>
                    </template>
                  </Carousel>
                </div>
                <div class="main-card">
                  <h5 :style="{ textAlign: 'mid' }">Cluster1</h5>
                  <Carousel
                    :value="cluster1.slice(0, 8)"
                    :numVisible="3"
                    :numScroll="2"
                  >
                    <template #item="slotProps">
                      <div class="cell-item">
                        <div>
                          <div class="image-wrapper-carousel">
                            <img
                              class="cell-image"
                              :src="'data:image/png;base64,' + slotProps.data"
                              alt="Valid cell"
                            />
                          </div>
                        </div>
                      </div>
                    </template>
                  </Carousel>
                </div>
                <div class="main-card">
                  <h5 :style="{ textAlign: 'mid' }">Cluster2</h5>
                  <Carousel
                    :value="cluster2.slice(0, 8)"
                    :numVisible="3"
                    :numScroll="2"
                  >
                    <template #item="slotProps">
                      <div class="cell-item">
                        <div>
                          <div class="image-wrapper-carousel">
                            <img
                              class="cell-image"
                              :src="'data:image/png;base64,' + slotProps.data"
                              alt="Valid cell"
                            />
                          </div>
                        </div>
                      </div>
                    </template>
                  </Carousel>
                </div>
                <div class="main-card">
                  <h5 :style="{ textAlign: 'mid' }">Cluster3</h5>
                  <Carousel
                    :value="cluster3.slice(0, 8)"
                    :numVisible="3"
                    :numScroll="2"
                  >
                    <template #item="slotProps">
                      <div class="cell-item">
                        <div>
                          <div class="image-wrapper-carousel">
                            <img
                              class="cell-image"
                              :src="'data:image/png;base64,' + slotProps.data"
                              alt="Valid cell"
                            />
                          </div>
                        </div>
                      </div>
                    </template>
                  </Carousel>
                </div>
              </SplitterPanel>
            </Splitter>
          </AccordionTab>
        </Accordion>
      </div>
    </div>
  </div>
</template>
<script type="module">
import Plotly from "plotly.js-dist-min";
import { APIService as cgAPIService } from "../api/cytometrygatingAPI";
export default {
  props: {
    msg: String,
  },
  data() {
    return {
      selectedAlgo: { name: "Mean Shift", code: "meanshift" },
      clusterAlgo: [
        { name: "Mean Shift", code: "meanshift" },
        { name: "KMean", code: "kmean" },
        { name: "Spectral", code: "spectral" },
        { name: "Agglomerative", code: "agglomerative" },
        { name: "Birch", code: "birch" },
      ],
      manualSelectedFeatureX1: { name: "Dissimilarity", code: "dissimilarity" },
      manualSelectedFeatureY1: { name: "Correlation", code: "correlation" },

      manualSelectedFeatureX2: { name: "Dissimilarity", code: "dissimilarity" },
      manualSelectedFeatureY2: { name: "Correlation", code: "correlation" },

      manualSelectedFeatureX3: { name: "Dissimilarity", code: "dissimilarity" },
      manualSelectedFeatureY3: { name: "Correlation", code: "correlation" },

      manualSelectedFeatureX4: { name: "Dissimilarity", code: "dissimilarity" },
      manualSelectedFeatureY4: { name: "Correlation", code: "correlation" },

      manualSelectedFeatureX5: { name: "Dissimilarity", code: "dissimilarity" },
      manualSelectedFeatureY5: { name: "Correlation", code: "correlation" },

      aiSelectedFeatureX: { name: "Dissimilarity", code: "dissimilarity" },
      aiSelectedFeatureY: { name: "Correlation", code: "correlation" },
      feature_selection: [
        { name: "Area", code: "area" },
        { name: "Aspect Ratio", code: "aspect_ratio" },
        { name: "Biconcavity", code: "biconcavity" },
        { name: "Circularity", code: "circularity" },
        { name: "Contrast", code: "contrast" },
        { name: "Correlation", code: "correlation" },
        { name: "Dissimilarity", code: "dissimilarity" },
        { name: "Energy", code: "energy" },
        { name: "Entropy", code: "entropy" },
        { name: "Equivalent Diameter", code: "equivalent_diameter" },
        { name: "Height", code: "height" },
        { name: "Homogeneity", code: "homogeneity" },
        { name: "Mass Center Shift", code: "mass_center_shift" },
        { name: "Optical Height Max", code: "optical_height_max" },
        { name: "Optical Height Min", code: "optical_height_min" },
        { name: "Optical Height Mean", code: "optical_height_mean" },
        { name: "Optical Height Var", code: "optical_height_var" },
        { name: "Perimeter", code: "perimeter" },
        { name: "Radius Mean", code: "radius_mean" },
        { name: "Radius Var", code: "radius_var" },
        { name: "Solidity", code: "solidity" },
        { name: "Sphericity", code: "sphericity" },
        { name: "Volume", code: "volume" },
        { name: "Width", code: "width" },
      ],
      Data: [],
      ClusterData: [],
      CellTypeInfo: [],
      LymImgs: [],
      MonImgs: [],
      EosImgs: [],
      NeuImgs: [],
      DataForSP2: [],
      DataForSP4: [],
      DataForSP5: [],
      ClickImg: [],
      particularScatterCellVisible: false,
      Tab2Visible: false,
      Tab3Visible: false,
      Tab4Visible: false,
      Tab5Visible: false,
      cluster0: [],
      cluster1: [],
      cluster2: [],
      cluster3: [],
      Labels: ["lym", "mon", "eos", "neu"],
      Values2: [],
      Values3: [],
      Values4: [],
      Values5: [],
      EvaluationData: [],
      CellTypeInfo1: [],
      CellTypeInfo2: [],
      CellTypeInfo3: [],
      CellTypeInfo4: [],
      Colors: ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"],
      config: {
        displaylogo: false,
        modeBarButtonsToRemove: [
          "zoom",
          "select2d",
          "lasso2d",
          "pan",
          "zoomIn2d",
          "zoomOut2d",
        ],
      },
      scatterPlotForTrace: [],
      clusterConfig: {
        displaylogo: false,
        modeBarButtonsToRemove: ["zoom", "select2d"],
      },
    };
  },
  computed: {
    cgAS: function () {
      return new cgAPIService();
    },
  },
  methods: {
    CellType() {
      this.CellTypeInfo = [
        { title: "lym", details: 78 },
        { title: "mon", details: 59 },
        { title: "eos", details: 42 },
        { title: "neu", details: 269 },
      ];
      var ultimateColors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"];
      var allLabels = ["lym", "mon", "eos", "neu"];
      var allValues = [78, 59, 42, 269];

      var piedata = [
        {
          values: allValues,
          labels: this.Labels,
          type: "pie",
          marker: { colors: this.Colors },
        },
      ];
      var pielayout = {
        autosize: true,
        title: "Types & Ratios",
      };
      Plotly.newPlot("PieChart", piedata, pielayout, this.config);
      var bardata = [
        {
          x: allLabels,
          y: allValues,
          type: "bar",
          marker: { color: ultimateColors },
        },
      ];
      var barlayout = {
        autosize: true,
        title: "Types & Number",
        xaxis: {
          title: "Types",
        },
        yaxis: {
          title: "Number",
        },
      };
      Plotly.newPlot("BarChart", bardata, barlayout, this.config);
    },

    //Show single Image after click point
    ShowImg(eventData) {
      if (eventData.points[0].curveNumber == 0) {
        this.cgAS
          .getImgs("lym", eventData.points[0].pointNumber)
          .then((info) => {
            this.ClickImg = info;
            this.particularScatterCellVisible = true;
          });
      } else if (eventData.points[0].curveNumber == 1) {
        this.cgAS
          .getImgs("mon", eventData.points[0].pointNumber)
          .then((info) => {
            this.ClickImg = info;
            this.particularScatterCellVisible = true;
          });
      } else if (eventData.points[0].curveNumber == 2) {
        this.cgAS
          .getImgs("eos", eventData.points[0].pointNumber)
          .then((info) => {
            this.ClickImg = info;
            this.particularScatterCellVisible = true;
          });
      } else if (eventData.points[0].curveNumber == 3) {
        this.cgAS
          .getImgs("neu", eventData.points[0].pointNumber)
          .then((info) => {
            this.ClickImg = info;
            this.particularScatterCellVisible = true;
          });
      }
    },
    //Plot scatter for 1.Step Manual Gating
    ScatterPlot(FeatureSelector_X, FeatureSelector_Y) {
      this.cgAS.getFeature().then((info) => {
        this.Data = info;
        var Keys = [];
        var cellValues = [];
        for (var i = 0; i < Object.keys(this.Data).length; i++) {
          Keys.push(Object.keys(this.Data)[i]);
          cellValues.push(this.Data[Object.keys(this.Data)[i]]);
        }
        var trace0 = {
          x: Object.values(this.Data[FeatureSelector_X]).slice(0, 78),
          y: Object.values(this.Data[FeatureSelector_Y]).slice(0, 78),
          xaxis: "x",
          yaxis: "y",
          mode: "markers",
          type: "scatter",
          name: "lym",
          marker: { color: "#1f77b4" },
        };
        var trace1 = {
          x: Object.values(this.Data[FeatureSelector_X]).slice(78, 137),
          y: Object.values(this.Data[FeatureSelector_Y]).slice(78, 137),
          xaxis: "x",
          yaxis: "y",
          mode: "markers",
          type: "scatter",
          name: "mon",
          marker: { color: "#ff7f0e" },
        };
        var trace2 = {
          x: Object.values(this.Data[FeatureSelector_X]).slice(137, 179),
          y: Object.values(this.Data[FeatureSelector_Y]).slice(137, 179),
          xaxis: "x",
          yaxis: "y",
          mode: "markers",
          type: "scatter",
          name: "eos",
          marker: { color: "#2ca02c" },
        };
        var trace3 = {
          x: Object.values(this.Data[FeatureSelector_X]).slice(179, 448),
          y: Object.values(this.Data[FeatureSelector_Y]).slice(179, 448),
          xaxis: "x",
          yaxis: "y",
          mode: "markers",
          type: "scatter",
          name: "neu",
          marker: { color: "#d62728" },
        };
        var data = [trace0, trace1, trace2, trace3];
        var layout = {
          grid: { rows: 1, columns: 1, pattern: "independent" },
          title:
            this.manualSelectedFeatureX1.name +
            " " +
            "&" +
            " " +
            this.manualSelectedFeatureY1.name,
          dragmode: "lasso",
          autosize: true,
          xaxis: {
            zeroline: false,
            automargin: true,
            title: this.manualSelectedFeatureX1.name,
          },
          yaxis: { title: this.manualSelectedFeatureY1.name, automargin: true },
        };
        Plotly.newPlot("ScatterPlot", data, layout, this.clusterConfig);
        var graphDiv = document.getElementById("ScatterPlot");
        graphDiv.on("plotly_selected", this.ScatterPlotCallback, false);
        graphDiv.on("plotly_click", this.ShowImg, false);
        var trace00 = {
          text: "sample length: 9",
          meanline: { visible: true },
          legendgroup: "F",
          scalegroup: "F",
          points: "none",
          box: { visible: true },
          jitter: 0,
          scalemode: "count",
          marker: { line: { width: 2, color: "#ff7f0e" }, symbol: "line-ns" },
          showlegend: false,
          type: "violin",
          name: FeatureSelector_Y,
          span: [0],
          line: { color: "#ff7f0e" },
          x0: "mon",
          y: Object.values(this.Data[FeatureSelector_Y]).slice(78, 137),
          orientation: "v",
        };
        var trace01 = {
          text: "sample length: 9",
          meanline: { visible: true },
          legendgroup: "F",
          scalegroup: "F",
          points: "none",
          box: { visible: true },
          jitter: 0,
          scalemode: "count",
          marker: { line: { width: 2, color: "#1f77b4" }, symbol: "line-ns" },
          showlegend: false,
          type: "violin",
          name: FeatureSelector_Y,
          span: [0],
          line: { color: "#1f77b4" },
          x0: "lym",
          y: Object.values(this.Data[FeatureSelector_Y]).slice(137, 179),
          orientation: "v",
        };
        var trace02 = {
          text: "sample length: 9",
          meanline: { visible: true },
          legendgroup: "F",
          scalegroup: "F",
          points: "none",
          box: { visible: true },
          jitter: 0,
          scalemode: "count",
          marker: { line: { width: 2, color: "#2ca02c" }, symbol: "line-ns" },
          showlegend: false,
          type: "violin",
          name: FeatureSelector_Y,
          span: [0],
          line: { color: "#2ca02c" },
          x0: "eos",
          y: Object.values(this.Data[FeatureSelector_Y]).slice(137, 179),
          orientation: "v",
        };
        var trace03 = {
          text: "sample length: 9",
          meanline: { visible: true },
          legendgroup: "F",
          scalegroup: "F",
          points: "none",
          box: { visible: true },
          jitter: 0,
          scalemode: "count",
          marker: { line: { width: 2, color: "#d62728" }, symbol: "line-ns" },
          showlegend: false,
          type: "violin",
          name: FeatureSelector_Y,
          span: [0],
          line: { color: "#d62728" },
          x0: "neu",
          y: Object.values(this.Data[FeatureSelector_Y]).slice(179, 448),
          orientation: "v",
        };
        var data0 = [trace00, trace01, trace02, trace03];
        var layout0 = {
          autosize: true,
          hovermode: "closest",
          yaxis: { showgrid: true, title: this.manualSelectedFeatureY1.name },
          xaxis: { title: "Types" },
          title: this.manualSelectedFeatureY1.name + " " + "of 1.Step",
          legend: { tracegroupgap: 0 },
          violingap: 0,
          violingroupgap: 0,
          violinmode: "overlay",
          height: 700,
        };
        Plotly.newPlot("violin", data0, layout0, this.config);

        var trace10 = {
          y: Object.values(this.Data[FeatureSelector_X]).slice(0, 78),
          type: "box",
          name: "lym",
          marker: { color: "#1f77b4" },
          boxpoints: "Outliers",
        };
        var trace11 = {
          y: Object.values(this.Data[FeatureSelector_X]).slice(78, 137),
          type: "box",
          name: "mon",
          marker: { color: "#ff7f0e" },
          boxpoints: "Outliers",
        };
        var trace12 = {
          y: Object.values(this.Data[FeatureSelector_X]).slice(137, 179),
          type: "box",
          name: "eos",
          marker: { color: "#2ca02c" },
          boxpoints: "Outliers",
        };
        var trace13 = {
          y: Object.values(this.Data[FeatureSelector_X]).slice(179, 448),
          type: "box",
          name: "neu",
          marker: { color: "#d62728" },
          boxpoints: "Outliers",
        };
        var data1 = [trace10, trace11, trace12, trace13];
        var layout1 = {
          autosize: true,
          title: this.manualSelectedFeatureX1.name + " " + "of 1.Step",
          xaxis: { title: "Types" },
          yaxis: { title: this.manualSelectedFeatureX1.name },
        }; //,width: 400,height: 400,
        Plotly.newPlot("boxplot", data1, layout1, this.config);
        this.CellTypeInfo1 = [
          { title: "lym", details: (1 * 100).toFixed(2) + "%" },
          { title: "mon", details: (1 * 100).toFixed(2) + "%" },
          { title: "eos", details: (1 * 100).toFixed(2) + "%" },
          { title: "neu", details: (1 * 100).toFixed(2) + "%" },
        ];
        var allValues = [78, 59, 42, 269];
        var bardata = [
          {
            x: this.Labels,
            y: allValues,
            type: "bar",
            marker: { color: this.Colors },
          },
        ];
        var layoutbar = {
          autosize: true,
          width: 400,
          height: 400,
          xaxis: { title: "Types" },
          yaxis: { title: "Number" },
          title: "Types & Number of 1.Step",
        };
        Plotly.newPlot("BarChart1", bardata, layoutbar, this.config);
        var piedata = [
          {
            values: allValues,
            labels: this.Labels,
            type: "pie",
            marker: { colors: this.Colors },
          },
        ];
        var layoutpie = {
          autosize: true,
          width: 400,
          height: 400,
          title: "Types & Ratios of 1.Step",
        };
        Plotly.newPlot("PieChart1", piedata, layoutpie, this.config);
      });
    },
    //Plot scatter for 2.Step Manual Gating
    ScatterPlot2(FeatureSelector_X, FeatureSelector_Y) {
      var trace0 = {
        x: Object.values(this.DataForSP2[FeatureSelector_X]).slice(0, 78),
        y: Object.values(this.DataForSP2[FeatureSelector_Y]).slice(0, 78),
        xaxis: "x",
        yaxis: "y",
        mode: "markers",
        type: "scatter",
        name: "lym",
        marker: { color: "#1f77b4" },
      };
      var trace1 = {
        x: Object.values(this.DataForSP2[FeatureSelector_X]).slice(78, 137),
        y: Object.values(this.DataForSP2[FeatureSelector_Y]).slice(78, 137),
        xaxis: "x",
        yaxis: "y",
        mode: "markers",
        type: "scatter",
        name: "mon",
        marker: { color: "#ff7f0e" },
      };
      var trace2 = {
        x: Object.values(this.DataForSP2[FeatureSelector_X]).slice(137, 179),
        y: Object.values(this.DataForSP2[FeatureSelector_Y]).slice(137, 179),
        xaxis: "x",
        yaxis: "y",
        mode: "markers",
        type: "scatter",
        name: "eos",
        marker: { color: "#2ca02c" },
      };
      var trace3 = {
        x: Object.values(this.DataForSP2[FeatureSelector_X]).slice(179, 448),
        y: Object.values(this.DataForSP2[FeatureSelector_Y]).slice(179, 448),
        xaxis: "x",
        yaxis: "y",
        mode: "markers",
        type: "scatter",
        name: "neu",
        marker: { color: "#d62728" },
      };
      var data = [trace0, trace1, trace2, trace3];
      var layout = {
        grid: { rows: 1, columns: 1, pattern: "independent" },
        title:
          this.manualSelectedFeatureX2.name +
          " " +
          "&" +
          " " +
          this.manualSelectedFeatureY2.name,
        dragmode: "lasso",
        autosize: true,
        xaxis: {
          zeroline: false,
          automargin: true,
          title: this.manualSelectedFeatureX2.name,
        },
        yaxis: { title: this.manualSelectedFeatureY2.name, automargin: true },
      };
      Plotly.newPlot("ScatterPlot2", data, layout, this.clusterConfig);
      var graphDiv = document.getElementById("ScatterPlot2");
      graphDiv.on("plotly_selected", this.ScatterPlot2Callback, false);
      graphDiv.on("plotly_click", this.ShowImg, false);

      var trace00 = {
        text: "sample length: 9",
        meanline: { visible: true },
        legendgroup: "F",
        scalegroup: "F",
        points: "none",
        box: { visible: true },
        jitter: 0,
        scalemode: "count",
        marker: { line: { width: 2, color: "#ff7f0e" }, symbol: "line-ns" },
        showlegend: false,
        type: "violin",
        name: FeatureSelector_Y,
        span: [0],
        line: { color: "#ff7f0e" },
        x0: "mon",
        y: Object.values(this.DataForSP2[FeatureSelector_Y]).slice(78, 137),
        orientation: "v",
      };
      var trace01 = {
        text: "sample length: 9",
        meanline: { visible: true },
        legendgroup: "F",
        scalegroup: "F",
        points: "none",
        box: { visible: true },
        jitter: 0,
        scalemode: "count",
        marker: { line: { width: 2, color: "#1f77b4" }, symbol: "line-ns" },
        showlegend: false,
        type: "violin",
        name: FeatureSelector_Y,
        span: [0],
        line: { color: "#1f77b4" },
        x0: "lym",
        y: Object.values(this.DataForSP2[FeatureSelector_Y]).slice(137, 179),
        orientation: "v",
      };
      var trace02 = {
        text: "sample length: 9",
        meanline: { visible: true },
        legendgroup: "F",
        scalegroup: "F",
        points: "none",
        box: { visible: true },
        jitter: 0,
        scalemode: "count",
        marker: { line: { width: 2, color: "#2ca02c" }, symbol: "line-ns" },
        showlegend: false,
        type: "violin",
        name: FeatureSelector_Y,
        span: [0],
        line: { color: "#2ca02c" },
        x0: "eos",
        y: Object.values(this.DataForSP2[FeatureSelector_Y]).slice(137, 179),
        orientation: "v",
      };
      var trace03 = {
        text: "sample length: 9",
        meanline: { visible: true },
        legendgroup: "F",
        scalegroup: "F",
        points: "none",
        box: { visible: true },
        jitter: 0,
        scalemode: "count",
        marker: { line: { width: 2, color: "#d62728" }, symbol: "line-ns" },
        showlegend: false,
        type: "violin",
        name: FeatureSelector_Y,
        span: [0],
        line: { color: "#d62728" },
        x0: "neu",
        y: Object.values(this.DataForSP2[FeatureSelector_Y]).slice(179, 448),
        orientation: "v",
      };
      var data0 = [trace00, trace01, trace02, trace03];
      var layout0 = {
        autosize: true,
        hovermode: "closest",
        yaxis: { showgrid: true, title: this.manualSelectedFeatureY2.name },
        xaxis: { title: "Types" },
        title: this.manualSelectedFeatureY2.name + " " + "of 2.Step",
        legend: { tracegroupgap: 0 },
        violingap: 0,
        violingroupgap: 0,
        violinmode: "overlay",
        height: 700,
      };
      Plotly.newPlot("Violin2", data0, layout0, this.config);

      var trace10 = {
        y: Object.values(this.DataForSP2[FeatureSelector_X]).slice(0, 78),
        type: "box",
        name: "lym",
        marker: { color: "#1f77b4" },
        boxpoints: "Outliers",
      };
      var trace11 = {
        y: Object.values(this.DataForSP2[FeatureSelector_X]).slice(78, 137),
        type: "box",
        name: "mon",
        marker: { color: "#ff7f0e" },
        boxpoints: "Outliers",
      };
      var trace12 = {
        y: Object.values(this.DataForSP2[FeatureSelector_X]).slice(137, 179),
        type: "box",
        name: "eos",
        marker: { color: "#2ca02c" },
        boxpoints: "Outliers",
      };
      var trace13 = {
        y: Object.values(this.DataForSP2[FeatureSelector_X]).slice(179, 448),
        type: "box",
        name: "neu",
        marker: { color: "#d62728" },
        boxpoints: "Outliers",
      };
      var data1 = [trace10, trace11, trace12, trace13];
      var layout1 = {
        autosize: true,
        title: this.manualSelectedFeatureX2.name + " " + "of 2.Step",
        xaxis: { title: "Types" },
        yaxis: { title: this.manualSelectedFeatureX2.name },
      };
      Plotly.newPlot("BoxPlot2", data1, layout1, this.config);
      var allValues = this.Values2;
      var bardata = [
        {
          x: this.Labels,
          y: allValues,
          type: "bar",
          marker: { color: this.Colors },
        },
      ];
      var layoutbar = {
        autosize: true,
        width: 400,
        height: 400,
        xaxis: { title: "Types" },
        yaxis: { title: "Number" },
        title: "Types & Number of 2.Step",
      };
      Plotly.newPlot("BarChart2", bardata, layoutbar, this.config);
      var piedata = [
        {
          values: allValues,
          labels: this.Labels,
          type: "pie",
          marker: { colors: this.Colors },
        },
      ];
      var layoutpie = {
        autosize: true,
        width: 400,
        height: 400,
        title: "Types & Ratios of 2.Step",
      };
      Plotly.newPlot("PieChart2", piedata, layoutpie, { displaylogo: false });

      this.CellTypeInfo2 = [
        {
          title: "lym",
          details: ((this.Values2[0] / 78) * 100).toFixed(2) + "%",
        },
        {
          title: "mon",
          details: ((this.Values2[1] / 59) * 100).toFixed(2) + "%",
        },
        {
          title: "eos",
          details: ((this.Values2[2] / 42) * 100).toFixed(2) + "%",
        },
        {
          title: "neu",
          details: ((this.Values2[3] / 269) * 100).toFixed(2) + "%",
        },
      ];
      this.Tab2Visible = true;
    },
    //Plot scatter for 3.Step Manual Gating
    ScatterPlot3(FeatureSelector_X, FeatureSelector_Y) {
      var trace0 = {
        x: Object.values(this.DataForSP3[FeatureSelector_X]).slice(0, 78),
        y: Object.values(this.DataForSP3[FeatureSelector_Y]).slice(0, 78),
        xaxis: "x",
        yaxis: "y",
        mode: "markers",
        type: "scatter",
        name: "lym",
        marker: { color: "#1f77b4" },
      };
      var trace1 = {
        x: Object.values(this.DataForSP3[FeatureSelector_X]).slice(78, 137),
        y: Object.values(this.DataForSP3[FeatureSelector_Y]).slice(78, 137),
        xaxis: "x",
        yaxis: "y",
        mode: "markers",
        type: "scatter",
        name: "mon",
        marker: { color: "#ff7f0e" },
      };
      var trace2 = {
        x: Object.values(this.DataForSP3[FeatureSelector_X]).slice(137, 179),
        y: Object.values(this.DataForSP3[FeatureSelector_Y]).slice(137, 179),
        xaxis: "x",
        yaxis: "y",
        mode: "markers",
        type: "scatter",
        name: "eos",
        marker: { color: "#2ca02c" },
      };
      var trace3 = {
        x: Object.values(this.DataForSP3[FeatureSelector_X]).slice(179, 448),
        y: Object.values(this.DataForSP3[FeatureSelector_Y]).slice(179, 448),
        xaxis: "x",
        yaxis: "y",
        mode: "markers",
        type: "scatter",
        name: "neu",
        marker: { color: "#d62728" },
      };
      var data = [trace0, trace1, trace2, trace3];
      var layout = {
        grid: { rows: 1, columns: 1, pattern: "independent" },
        title:
          this.manualSelectedFeatureX3.name +
          " " +
          "&" +
          " " +
          this.manualSelectedFeatureY3.name,
        dragmode: "lasso",
        autosize: true,
        xaxis: {
          zeroline: false,
          automargin: true,
          title: this.manualSelectedFeatureX3.name,
        },
        yaxis: { title: this.manualSelectedFeatureY3.name, automargin: true },
      };
      Plotly.newPlot("ScatterPlot3", data, layout, this.clusterConfig);
      var graphDiv = document.getElementById("ScatterPlot3");
      graphDiv.on("plotly_selected", this.ScatterPlot3Callback, false);
      graphDiv.on("plotly_click", this.ShowImg, false);

      var trace00 = {
        text: "sample length: 9",
        meanline: { visible: true },
        legendgroup: "F",
        scalegroup: "F",
        points: "none",
        box: { visible: true },
        jitter: 0,
        scalemode: "count",
        marker: { line: { width: 2, color: "#ff7f0e" }, symbol: "line-ns" },
        showlegend: false,
        type: "violin",
        name: FeatureSelector_Y,
        span: [0],
        line: { color: "#ff7f0e" },
        x0: "mon",
        y: Object.values(this.DataForSP3[FeatureSelector_Y]).slice(78, 137),
        orientation: "v",
      };
      var trace01 = {
        text: "sample length: 9",
        meanline: { visible: true },
        legendgroup: "F",
        scalegroup: "F",
        points: "none",
        box: { visible: true },
        jitter: 0,
        scalemode: "count",
        marker: { line: { width: 2, color: "#1f77b4" }, symbol: "line-ns" },
        showlegend: false,
        type: "violin",
        name: FeatureSelector_Y,
        span: [0],
        line: { color: "#1f77b4" },
        x0: "lym",
        y: Object.values(this.DataForSP3[FeatureSelector_Y]).slice(137, 179),
        orientation: "v",
      };
      var trace02 = {
        text: "sample length: 9",
        meanline: { visible: true },
        legendgroup: "F",
        scalegroup: "F",
        points: "none",
        box: { visible: true },
        jitter: 0,
        scalemode: "count",
        marker: { line: { width: 2, color: "#2ca02c" }, symbol: "line-ns" },
        showlegend: false,
        type: "violin",
        name: FeatureSelector_Y,
        span: [0],
        line: { color: "#2ca02c" },
        x0: "eos",
        y: Object.values(this.DataForSP3[FeatureSelector_Y]).slice(137, 179),
        orientation: "v",
      };
      var trace03 = {
        text: "sample length: 9",
        meanline: { visible: true },
        legendgroup: "F",
        scalegroup: "F",
        points: "none",
        box: { visible: true },
        jitter: 0,
        scalemode: "count",
        marker: { line: { width: 2, color: "#d62728" }, symbol: "line-ns" },
        showlegend: false,
        type: "violin",
        name: FeatureSelector_Y,
        span: [0],
        line: { color: "#d62728" },
        x0: "neu",
        y: Object.values(this.DataForSP3[FeatureSelector_Y]).slice(179, 448),
        orientation: "v",
      };
      var data0 = [trace00, trace01, trace02, trace03];
      var layout0 = {
        autosize: true,
        hovermode: "closest",
        yaxis: { showgrid: true, title: this.manualSelectedFeatureY3.name },
        xaxis: { title: "Types" },
        title: this.manualSelectedFeatureY3.name + " " + "of 3.Step",
        legend: { tracegroupgap: 0 },
        violingap: 0,
        violingroupgap: 0,
        violinmode: "overlay",
        height: 700,
      };
      Plotly.newPlot("Violin3", data0, layout0, this.config);

      var trace10 = {
        y: Object.values(this.DataForSP3[FeatureSelector_X]).slice(0, 78),
        type: "box",
        name: "lym",
        marker: { color: "#1f77b4" },
        boxpoints: "Outliers",
      };
      var trace11 = {
        y: Object.values(this.DataForSP3[FeatureSelector_X]).slice(78, 137),
        type: "box",
        name: "mon",
        marker: { color: "#ff7f0e" },
        boxpoints: "Outliers",
      };
      var trace12 = {
        y: Object.values(this.DataForSP3[FeatureSelector_X]).slice(137, 179),
        type: "box",
        name: "eos",
        marker: { color: "#2ca02c" },
        boxpoints: "Outliers",
      };
      var trace13 = {
        y: Object.values(this.DataForSP3[FeatureSelector_X]).slice(179, 448),
        type: "box",
        name: "neu",
        marker: { color: "#d62728" },
        boxpoints: "Outliers",
      };
      var data1 = [trace10, trace11, trace12, trace13];
      var layout1 = {
        autosize: true,
        title: this.manualSelectedFeatureX3.name + " " + "of 3.Step",
        xaxis: { title: "Types" },
        yaxis: { title: this.manualSelectedFeatureX3.name },
      };
      Plotly.newPlot("BoxPlot3", data1, layout1, this.config);

      var allValues = this.Values3;
      var bardata = [
        {
          x: this.Labels,
          y: allValues,
          type: "bar",
          marker: { color: this.Colors },
        },
      ];
      var layoutbar = {
        autosize: true,
        width: 400,
        height: 400,
        xaxis: { title: "Types" },
        yaxis: { title: "Number" },
        title: "Types & Number of 3.Step",
      };
      Plotly.newPlot("BarChart3", bardata, layoutbar, this.config);
      var piedata = [
        {
          values: allValues,
          labels: this.Labels,
          type: "pie",
          marker: { colors: this.Colors },
        },
      ];
      var layoutpie = {
        autosize: true,
        width: 400,
        height: 400,
        title: "Types & Ratios of 3.Step",
      };
      Plotly.newPlot("PieChart3", piedata, layoutpie, { displaylogo: false });
      this.CellTypeInfo3 = [
        {
          title: "lym",
          details: ((this.Values3[0] / 78) * 100).toFixed(2) + "%",
        },
        {
          title: "mon",
          details: ((this.Values3[1] / 59) * 100).toFixed(2) + "%",
        },
        {
          title: "eos",
          details: ((this.Values3[2] / 42) * 100).toFixed(2) + "%",
        },
        {
          title: "neu",
          details: ((this.Values3[3] / 269) * 100).toFixed(2) + "%",
        },
      ];
      this.Tab3Visible = true;
    },
    //Plot scatter for 4.Step Manual Gating
    ScatterPlot4(FeatureSelector_X, FeatureSelector_Y) {
      var trace0 = {
        x: Object.values(this.DataForSP4[FeatureSelector_X]).slice(0, 78),
        y: Object.values(this.DataForSP4[FeatureSelector_Y]).slice(0, 78),
        xaxis: "x",
        yaxis: "y",
        mode: "markers",
        type: "scatter",
        name: "lym",
        marker: { color: "#1f77b4" },
      };
      var trace1 = {
        x: Object.values(this.DataForSP4[FeatureSelector_X]).slice(78, 137),
        y: Object.values(this.DataForSP4[FeatureSelector_Y]).slice(78, 137),
        xaxis: "x",
        yaxis: "y",
        mode: "markers",
        type: "scatter",
        name: "mon",
        marker: { color: "#ff7f0e" },
      };
      var trace2 = {
        x: Object.values(this.DataForSP4[FeatureSelector_X]).slice(137, 179),
        y: Object.values(this.DataForSP4[FeatureSelector_Y]).slice(137, 179),
        xaxis: "x",
        yaxis: "y",
        mode: "markers",
        type: "scatter",
        name: "eos",
        marker: { color: "#2ca02c" },
      };
      var trace3 = {
        x: Object.values(this.DataForSP4[FeatureSelector_X]).slice(179, 448),
        y: Object.values(this.DataForSP4[FeatureSelector_Y]).slice(179, 448),
        xaxis: "x",
        yaxis: "y",
        mode: "markers",
        type: "scatter",
        name: "neu",
        marker: { color: "#d62728" },
      };
      var data = [trace0, trace1, trace2, trace3];
      var layout = {
        grid: { rows: 1, columns: 1, pattern: "independent" },
        title:
          this.manualSelectedFeatureX4.name +
          " " +
          "&" +
          " " +
          this.manualSelectedFeatureY4.name,
        dragmode: "lasso",
        autosize: true,
        xaxis: {
          zeroline: false,
          automargin: true,
          title: this.manualSelectedFeatureX4.name,
        },
        yaxis: { title: this.manualSelectedFeatureY4.name, automargin: true },
      };
      Plotly.newPlot("ScatterPlot4", data, layout, this.clusterConfig);
      var graphDiv = document.getElementById("ScatterPlot4");
      graphDiv.on("plotly_selected", this.ScatterPlot4Callback, false);
      graphDiv.on("plotly_click", this.ShowImg, false);

      var trace00 = {
        text: "sample length: 9",
        meanline: { visible: true },
        legendgroup: "F",
        scalegroup: "F",
        points: "none",
        box: { visible: true },
        jitter: 0,
        scalemode: "count",
        marker: { line: { width: 2, color: "#ff7f0e" }, symbol: "line-ns" },
        showlegend: false,
        type: "violin",
        name: FeatureSelector_Y,
        span: [0],
        line: { color: "#ff7f0e" },
        x0: "mon",
        y: Object.values(this.DataForSP4[FeatureSelector_Y]).slice(78, 137),
        orientation: "v",
      };
      var trace01 = {
        text: "sample length: 9",
        meanline: { visible: true },
        legendgroup: "F",
        scalegroup: "F",
        points: "none",
        box: { visible: true },
        jitter: 0,
        scalemode: "count",
        marker: { line: { width: 2, color: "#1f77b4" }, symbol: "line-ns" },
        showlegend: false,
        type: "violin",
        name: FeatureSelector_Y,
        span: [0],
        line: { color: "#1f77b4" },
        x0: "lym",
        y: Object.values(this.DataForSP4[FeatureSelector_Y]).slice(137, 179),
        orientation: "v",
      };
      var trace02 = {
        text: "sample length: 9",
        meanline: { visible: true },
        legendgroup: "F",
        scalegroup: "F",
        points: "none",
        box: { visible: true },
        jitter: 0,
        scalemode: "count",
        marker: { line: { width: 2, color: "#2ca02c" }, symbol: "line-ns" },
        showlegend: false,
        type: "violin",
        name: FeatureSelector_Y,
        span: [0],
        line: { color: "#2ca02c" },
        x0: "eos",
        y: Object.values(this.DataForSP4[FeatureSelector_Y]).slice(137, 179),
        orientation: "v",
      };
      var trace03 = {
        text: "sample length: 9",
        meanline: { visible: true },
        legendgroup: "F",
        scalegroup: "F",
        points: "none",
        box: { visible: true },
        jitter: 0,
        scalemode: "count",
        marker: { line: { width: 2, color: "#d62728" }, symbol: "line-ns" },
        showlegend: false,
        type: "violin",
        name: FeatureSelector_Y,
        span: [0],
        line: { color: "#d62728" },
        x0: "neu",
        y: Object.values(this.DataForSP4[FeatureSelector_Y]).slice(179, 448),
        orientation: "v",
      };
      var data0 = [trace00, trace01, trace02, trace03];
      var layout0 = {
        autosize: true,
        hovermode: "closest",
        yaxis: { showgrid: true, title: this.manualSelectedFeatureY4.name },
        xaxis: { title: "Types" },
        title: this.manualSelectedFeatureY4.name + " " + "of 4.Step",
        legend: { tracegroupgap: 0 },
        violingap: 0,
        violingroupgap: 0,
        violinmode: "overlay",
        height: 700,
      };
      Plotly.newPlot("Violin4", data0, layout0, this.config);

      var allValues = this.Values4;
      var bardata = [
        {
          x: this.Labels,
          y: allValues,
          type: "bar",
          marker: { color: this.Colors },
        },
      ];
      var layoutbar = {
        autosize: true,
        width: 400,
        height: 400,
        xaxis: { title: "Types" },
        yaxis: { title: "Number" },
        title: "Types & Number of 4.Step",
      };
      Plotly.newPlot("BarChart4", bardata, layoutbar, this.config);
      var trace10 = {
        y: Object.values(this.DataForSP4[FeatureSelector_X]).slice(0, 78),
        type: "box",
        name: "lym",
        marker: { color: "#1f77b4" },
        boxpoints: "Outliers",
      };
      var trace11 = {
        y: Object.values(this.DataForSP4[FeatureSelector_X]).slice(78, 137),
        type: "box",
        name: "mon",
        marker: { color: "#ff7f0e" },
        boxpoints: "Outliers",
      };
      var trace12 = {
        y: Object.values(this.DataForSP4[FeatureSelector_X]).slice(137, 179),
        type: "box",
        name: "eos",
        marker: { color: "#2ca02c" },
        boxpoints: "Outliers",
      };
      var trace13 = {
        y: Object.values(this.DataForSP4[FeatureSelector_X]).slice(179, 448),
        type: "box",
        name: "neu",
        marker: { color: "#d62728" },
        boxpoints: "Outliers",
      };
      var data1 = [trace10, trace11, trace12, trace13];

      var layout1 = {
        autosize: true,
        title: this.manualSelectedFeatureX4.name + " " + "of 4.Step",
        xaxis: { title: "Types" },
        yaxis: { title: this.manualSelectedFeatureX4.name },
      };
      Plotly.newPlot("BoxPlot4", data1, layout1, this.config);

      var piedata = [
        {
          values: allValues,
          labels: this.Labels,
          type: "pie",
          marker: { colors: this.Colors },
        },
      ];
      var layoutpie = {
        autosize: true,
        width: 400,
        height: 400,
        title: "Types & Ratios of 4.Step",
      };
      Plotly.newPlot("PieChart4", piedata, layoutpie, { displaylogo: false });
      this.CellTypeInfo4 = [
        {
          title: "lym",
          details: ((this.Values4[0] / 78) * 100).toFixed(2) + "%",
        },
        {
          title: "mon",
          details: ((this.Values4[1] / 59) * 100).toFixed(2) + "%",
        },
        {
          title: "eos",
          details: ((this.Values4[2] / 42) * 100).toFixed(2) + "%",
        },
        {
          title: "neu",
          details: ((this.Values4[3] / 269) * 100).toFixed(2) + "%",
        },
      ];
      this.Tab4Visible = true;
    },
    //Plot scatter for 5.Step Manual Gating
    ScatterPlot5(FeatureSelector_X, FeatureSelector_Y) {
      var trace0 = {
        x: Object.values(this.DataForSP5[FeatureSelector_X]).slice(0, 78),
        y: Object.values(this.DataForSP5[FeatureSelector_Y]).slice(0, 78),
        xaxis: "x",
        yaxis: "y",
        mode: "markers",
        type: "scatter",
        name: "lym",
        marker: { color: "#1f77b4" },
      };
      var trace1 = {
        x: Object.values(this.DataForSP5[FeatureSelector_X]).slice(78, 137),
        y: Object.values(this.DataForSP5[FeatureSelector_Y]).slice(78, 137),
        xaxis: "x",
        yaxis: "y",
        mode: "markers",
        type: "scatter",
        name: "mon",
        marker: { color: "#ff7f0e" },
      };
      var trace2 = {
        x: Object.values(this.DataForSP5[FeatureSelector_X]).slice(137, 179),
        y: Object.values(this.DataForSP5[FeatureSelector_Y]).slice(137, 179),
        xaxis: "x",
        yaxis: "y",
        mode: "markers",
        type: "scatter",
        name: "eos",
        marker: { color: "#2ca02c" },
      };
      var trace3 = {
        x: Object.values(this.DataForSP5[FeatureSelector_X]).slice(179, 448),
        y: Object.values(this.DataForSP5[FeatureSelector_Y]).slice(179, 448),
        xaxis: "x",
        yaxis: "y",
        mode: "markers",
        type: "scatter",
        name: "neu",
        marker: { color: "#d62728" },
      };
      var data = [trace0, trace1, trace2, trace3];

      var layout = {
        grid: { rows: 1, columns: 1, pattern: "independent" },
        title:
          this.manualSelectedFeatureX5.name +
          " " +
          "&" +
          " " +
          this.manualSelectedFeatureY5.name,
        dragmode: "lasso",
        autosize: true,
        xaxis: {
          zeroline: false,
          automargin: true,
          title: this.manualSelectedFeatureX5.name,
        },
        yaxis: { title: this.manualSelectedFeatureY5.name, automargin: true },
      };
      Plotly.newPlot("ScatterPlot5", data, layout, this.clusterConfig);
      var graphDiv = document.getElementById("ScatterPlot5");
      graphDiv.on("plotly_click", this.ShowImg, false);
      graphDiv.on("plotly_selected", this.ScatterPlot5Callback, false);

      var trace00 = {
        text: "sample length: 9",
        meanline: { visible: true },
        legendgroup: "F",
        scalegroup: "F",
        points: "none",
        box: { visible: true },
        jitter: 0,
        scalemode: "count",
        marker: { line: { width: 2, color: "#ff7f0e" }, symbol: "line-ns" },
        showlegend: false,
        type: "violin",
        name: FeatureSelector_Y,
        span: [0],
        line: { color: "#ff7f0e" },
        x0: "mon",
        y: Object.values(this.DataForSP5[FeatureSelector_Y]).slice(78, 137),
        orientation: "v",
      };
      var trace01 = {
        text: "sample length: 9",
        meanline: { visible: true },
        legendgroup: "F",
        scalegroup: "F",
        points: "none",
        box: { visible: true },
        jitter: 0,
        scalemode: "count",
        marker: { line: { width: 2, color: "#1f77b4" }, symbol: "line-ns" },
        showlegend: false,
        type: "violin",
        name: FeatureSelector_Y,
        span: [0],
        line: { color: "#1f77b4" },
        x0: "lym",
        y: Object.values(this.DataForSP5[FeatureSelector_Y]).slice(137, 179),
        orientation: "v",
      };
      var trace02 = {
        text: "sample length: 9",
        meanline: { visible: true },
        legendgroup: "F",
        scalegroup: "F",
        points: "none",
        box: { visible: true },
        jitter: 0,
        scalemode: "count",
        marker: { line: { width: 2, color: "#2ca02c" }, symbol: "line-ns" },
        showlegend: false,
        type: "violin",
        name: FeatureSelector_Y,
        span: [0],
        line: { color: "#2ca02c" },
        x0: "eos",
        y: Object.values(this.DataForSP5[FeatureSelector_Y]).slice(137, 179),
        orientation: "v",
      };
      var trace03 = {
        text: "sample length: 9",
        meanline: { visible: true },
        legendgroup: "F",
        scalegroup: "F",
        points: "none",
        box: { visible: true },
        jitter: 0,
        scalemode: "count",
        marker: { line: { width: 2, color: "#d62728" }, symbol: "line-ns" },
        showlegend: false,
        type: "violin",
        name: FeatureSelector_Y,
        span: [0],
        line: { color: "#d62728" },
        x0: "neu",
        y: Object.values(this.DataForSP5[FeatureSelector_Y]).slice(179, 448),
        orientation: "v",
      };
      var data0 = [trace00, trace01, trace02, trace03];

      var layout0 = {
        autosize: true,
        hovermode: "closest",
        yaxis: { showgrid: true, title: this.manualSelectedFeatureY5.name },
        xaxis: { title: "Types" },
        title: this.manualSelectedFeatureY5.name + " " + "of 5.Step",
        legend: { tracegroupgap: 0 },
        violingap: 0,
        violingroupgap: 0,
        violinmode: "overlay",
        height: 700,
      };
      Plotly.newPlot("Violin5", data0, layout0, this.config);

      var trace10 = {
        y: Object.values(this.DataForSP5[FeatureSelector_X]).slice(0, 78),
        type: "box",
        name: "lym",
        marker: { color: "#1f77b4" },
        boxpoints: "Outliers",
      };
      var trace11 = {
        y: Object.values(this.DataForSP5[FeatureSelector_X]).slice(78, 137),
        type: "box",
        name: "mon",
        marker: { color: "#ff7f0e" },
        boxpoints: "Outliers",
      };
      var trace12 = {
        y: Object.values(this.DataForSP5[FeatureSelector_X]).slice(137, 179),
        type: "box",
        name: "eos",
        marker: { color: "#2ca02c" },
        boxpoints: "Outliers",
      };
      var trace13 = {
        y: Object.values(this.DataForSP5[FeatureSelector_X]).slice(179, 448),
        type: "box",
        name: "neu",
        marker: { color: "#d62728" },
        boxpoints: "Outliers",
      };
      var data1 = [trace10, trace11, trace12, trace13];

      var layout1 = {
        autosize: true,
        title: this.manualSelectedFeatureX5.name + " " + "of 5.Step",
        xaxis: { title: "Types" },
        yaxis: { title: this.manualSelectedFeatureX5.name },
      };

      Plotly.newPlot("BoxPlot5", data1, layout1, this.config);

      var allValues = this.Values5;
      var bardata = [
        {
          x: this.Labels,
          y: allValues,
          type: "bar",
          marker: { color: this.Colors },
        },
      ];
      var layoutbar = {
        autosize: true,
        width: 400,
        height: 400,
        xaxis: { title: "Types" },
        yaxis: { title: "Number" },
        title: "Types & Number of 5.Step",
      };
      Plotly.newPlot("BarChart5", bardata, layoutbar, this.config);
      var piedata = [
        {
          values: allValues,
          labels: this.Labels,
          type: "pie",
          marker: { colors: this.Colors },
        },
      ];
      var layoutpie = {
        autosize: true,
        width: 400,
        height: 400,
        title: "Types & Ratios of 5.Step",
      };
      Plotly.newPlot("PieChart5", piedata, layoutpie, { displaylogo: false });
      this.CellTypeInfo5 = [
        {
          title: "lym",
          details: ((this.Values5[0] / 78) * 100).toFixed(2) + "%",
        },
        {
          title: "mon",
          details: ((this.Values5[1] / 59) * 100).toFixed(2) + "%",
        },
        {
          title: "eos",
          details: ((this.Values5[2] / 42) * 100).toFixed(2) + "%",
        },
        {
          title: "neu",
          details: ((this.Values5[3] / 269) * 100).toFixed(2) + "%",
        },
      ];
      this.Tab5Visible = true;
    },
    //Prepare data for 2.Step Manual Gating
    ScatterPlotCallback(eventData) {
      var Index0 = [];
      var Index1 = [];
      var Index2 = [];
      var Index3 = [];
      for (var i = 0; i < eventData.points.length; i++) {
        if (eventData.points[i].curveNumber == 0) {
          Index0.push(eventData.points[i].pointIndex);
        } else if (eventData.points[i].curveNumber == 1) {
          Index1.push(eventData.points[i].pointIndex);
        } else if (eventData.points[i].curveNumber == 2) {
          Index2.push(eventData.points[i].pointIndex);
        } else if (eventData.points[i].curveNumber == 3) {
          Index3.push(eventData.points[i].pointIndex);
        }
      }
      var id0 = Index0;
      var id1 = Index1.map((x) => x + 78);
      var id2 = Index2.map((x) => x + 137);
      var id3 = Index3.map((x) => x + 179);

      var id = [].concat(id0, id1, id2, id3);
      this.cgAS.postNewData(id).then((info) => {
        this.DataForSP2 = info;
      });
      for (var i1 = 0; i1 < 4; i1++) {
        this.LymImgs.pop();
        this.MonImgs.pop();
        this.EosImgs.pop();
        this.NeuImgs.pop();
      }
      for (var i2 = 0; i2 < 4; i2++) {
        this.cgAS.getImgs("lym", Index0[i2]).then((info) => {
          this.LymImgs.push(info);
        });
        this.cgAS.getImgs("mon", Index1[i2]).then((info) => {
          this.MonImgs.push(info);
        });
        this.cgAS.getImgs("eos", Index2[i2]).then((info) => {
          this.EosImgs.push(info);
        });
        this.cgAS.getImgs("neu", Index3[i2]).then((info) => {
          this.NeuImgs.push(info);
        });
      }
      this.Values2 = [
        Index0.length,
        Index1.length,
        Index2.length,
        Index3.length,
      ];
    },
    //Prepare data for 3.Step Manual Gating
    ScatterPlot2Callback(eventData) {
      var Index0 = [];
      var Index1 = [];
      var Index2 = [];
      var Index3 = [];
      for (var i = 0; i < eventData.points.length; i++) {
        if (eventData.points[i].curveNumber == 0) {
          Index0.push(eventData.points[i].pointIndex);
        } else if (eventData.points[i].curveNumber == 1) {
          Index1.push(eventData.points[i].pointIndex);
        } else if (eventData.points[i].curveNumber == 2) {
          Index2.push(eventData.points[i].pointIndex);
        } else if (eventData.points[i].curveNumber == 3) {
          Index3.push(eventData.points[i].pointIndex);
        }
      }
      var id0 = Index0;
      var id1 = Index1.map((x) => x + 78);
      var id2 = Index2.map((x) => x + 137);
      var id3 = Index3.map((x) => x + 179);
      var id = [].concat(id0, id1, id2, id3);
      this.cgAS.postNewData(id).then((info) => {
        this.DataForSP3 = info;
      });
      for (var i1 = 0; i1 < 4; i1++) {
        this.LymImgs.pop();
        this.MonImgs.pop();
        this.EosImgs.pop();
        this.NeuImgs.pop();
      }
      for (var i2 = 0; i2 < 4; i2++) {
        this.cgAS.getImgs("lym", Index0[i2]).then((info) => {
          this.LymImgs.push(info);
        });
        this.cgAS.getImgs("mon", Index1[i2]).then((info) => {
          this.MonImgs.push(info);
        });
        this.cgAS.getImgs("eos", Index2[i2]).then((info) => {
          this.EosImgs.push(info);
        });
        this.cgAS.getImgs("neu", Index3[i2]).then((info) => {
          this.NeuImgs.push(info);
        });
      }
      this.Values3 = [
        Index0.length,
        Index1.length,
        Index2.length,
        Index3.length,
      ];
    },
    //Prepare data for 4.Step Manual Gating
    ScatterPlot3Callback(eventData) {
      var Index0 = [];
      var Index1 = [];
      var Index2 = [];
      var Index3 = [];
      for (var i = 0; i < eventData.points.length; i++) {
        if (eventData.points[i].curveNumber == 0) {
          Index0.push(eventData.points[i].pointIndex);
        } else if (eventData.points[i].curveNumber == 1) {
          Index1.push(eventData.points[i].pointIndex);
        } else if (eventData.points[i].curveNumber == 2) {
          Index2.push(eventData.points[i].pointIndex);
        } else if (eventData.points[i].curveNumber == 3) {
          Index3.push(eventData.points[i].pointIndex);
        }
      }
      var id0 = Index0;
      var id1 = Index1.map((x) => x + 78);
      var id2 = Index2.map((x) => x + 137);
      var id3 = Index3.map((x) => x + 179);
      var id = [].concat(id0, id1, id2, id3);
      this.cgAS.postNewData(id).then((info) => {
        this.DataForSP4 = info;
      });
      for (var i1 = 0; i1 < 4; i1++) {
        this.LymImgs.pop();
        this.MonImgs.pop();
        this.EosImgs.pop();
        this.NeuImgs.pop();
      }
      for (var i2 = 0; i2 < 4; i2++) {
        this.cgAS.getImgs("lym", Index0[i2]).then((info) => {
          this.LymImgs.push(info);
        });
        this.cgAS.getImgs("mon", Index1[i2]).then((info) => {
          this.MonImgs.push(info);
        });
        this.cgAS.getImgs("eos", Index2[i2]).then((info) => {
          this.EosImgs.push(info);
        });
        this.cgAS.getImgs("neu", Index3[i2]).then((info) => {
          this.NeuImgs.push(info);
        });
      }
      this.Values4 = [
        Index0.length,
        Index1.length,
        Index2.length,
        Index3.length,
      ];
    },
    //Prepare data for 5.Step Manual Gating
    ScatterPlot4Callback(eventData) {
      var Index0 = [];
      var Index1 = [];
      var Index2 = [];
      var Index3 = [];
      for (var i = 0; i < eventData.points.length; i++) {
        if (eventData.points[i].curveNumber == 0) {
          Index0.push(eventData.points[i].pointIndex);
        } else if (eventData.points[i].curveNumber == 1) {
          Index1.push(eventData.points[i].pointIndex);
        } else if (eventData.points[i].curveNumber == 2) {
          Index2.push(eventData.points[i].pointIndex);
        } else if (eventData.points[i].curveNumber == 3) {
          Index3.push(eventData.points[i].pointIndex);
        }
      }
      var id0 = Index0;
      var id1 = Index1.map((x) => x + 78);
      var id2 = Index2.map((x) => x + 137);
      var id3 = Index3.map((x) => x + 179);
      var id = [].concat(id0, id1, id2, id3);
      this.cgAS.postNewData(id).then((info) => {
        this.DataForSP5 = info;
      });
      for (var i1 = 0; i1 < 4; i1++) {
        this.LymImgs.pop();
        this.MonImgs.pop();
        this.EosImgs.pop();
        this.NeuImgs.pop();
      }
      for (var i2 = 0; i2 < 4; i2++) {
        this.cgAS.getImgs("lym", Index0[i2]).then((info) => {
          this.LymImgs.push(info);
        });
        this.cgAS.getImgs("mon", Index1[i2]).then((info) => {
          this.MonImgs.push(info);
        });
        this.cgAS.getImgs("eos", Index2[i2]).then((info) => {
          this.EosImgs.push(info);
        });
        this.cgAS.getImgs("neu", Index3[i2]).then((info) => {
          this.NeuImgs.push(info);
        });
      }
      this.Values5 = [
        Index0.length,
        Index1.length,
        Index2.length,
        Index3.length,
      ];
    },
    //Prepare data for end analyse
    ScatterPlot5Callback(eventData) {
      var Index0 = [];
      var Index1 = [];
      var Index2 = [];
      var Index3 = [];
      for (var i = 0; i < eventData.points.length; i++) {
        if (eventData.points[i].curveNumber == 0) {
          Index0.push(eventData.points[i].pointIndex);
        } else if (eventData.points[i].curveNumber == 1) {
          Index1.push(eventData.points[i].pointIndex);
        } else if (eventData.points[i].curveNumber == 2) {
          Index2.push(eventData.points[i].pointIndex);
        } else if (eventData.points[i].curveNumber == 3) {
          Index3.push(eventData.points[i].pointIndex);
        }
      }
      for (var i1 = 0; i1 < 4; i1++) {
        this.LymImgs.pop();
        this.MonImgs.pop();
        this.EosImgs.pop();
        this.NeuImgs.pop();
      }
      for (var i2 = 0; i2 < 4; i2++) {
        this.cgAS.getImgs("lym", Index0[i2]).then((info) => {
          this.LymImgs.push(info);
        });
        this.cgAS.getImgs("mon", Index1[i2]).then((info) => {
          this.MonImgs.push(info);
        });
        this.cgAS.getImgs("eos", Index2[i2]).then((info) => {
          this.EosImgs.push(info);
        });
        this.cgAS.getImgs("neu", Index3[i2]).then((info) => {
          this.NeuImgs.push(info);
        });
      }
    },
    //Plot scatter for Machine Learning supported Gating
    Cluster(clustertype, idx, idy) {
      this.cgAS.getClusterData(clustertype, idx, idy).then((info) => {
        this.ClusterData = info;
        this.EvaluationData = [
          {
            title: "Number of clusters",
            details: Object.values(this.ClusterData["ENC"])[0].toFixed(0),
          },
          {
            title: "Accuracy",
            details: Object.values(this.ClusterData["Accuracy"])[0].toFixed(3),
          },
          {
            title: "Homogeneity",
            details: Object.values(this.ClusterData["Homogeneity"])[0].toFixed(
              3
            ),
          },
          {
            title: "V-measure",
            details: Object.values(this.ClusterData["V_measure"])[0].toFixed(3),
          },
          {
            title: "Adjusted Rand Index",
            details: Object.values(
              this.ClusterData["Adjusted_Rand_Index"]
            )[0].toFixed(3),
          },
          {
            title: "Adjusted Mutual Information",
            details: Object.values(
              this.ClusterData["Adjusted_Mutual_Information"]
            )[0].toFixed(3),
          },
          {
            title: "Silhouette Coefficient",
            details: Object.values(
              this.ClusterData["Silhouette_Coefficient"]
            )[0].toFixed(3),
          },
        ];
        var Cluster0 = {
          x: Object.values(this.ClusterData["col0x"]),
          y: Object.values(this.ClusterData["col0y"]),
          mode: "markers",
          type: "scatter",
          name: "Cluster0",
        };
        var Cluster1 = {
          x: Object.values(this.ClusterData["col1x"]),
          y: Object.values(this.ClusterData["col1y"]),
          mode: "markers",
          type: "scatter",
          name: "Cluster1",
        };
        var Cluster2 = {
          x: Object.values(this.ClusterData["col2x"]),
          y: Object.values(this.ClusterData["col2y"]),
          mode: "markers",
          type: "scatter",
          name: "Cluster2",
        };
        var Cluster3 = {
          x: Object.values(this.ClusterData["col3x"]),
          y: Object.values(this.ClusterData["col3y"]),
          mode: "markers",
          type: "scatter",
          name: "Cluster3",
        };
        var data = [Cluster0, Cluster1, Cluster2, Cluster3];
        var layout = {
          // grid: { rows: 1, columns: 1, pattern: "independent" },
          title:
            this.selectedAlgo.name +
            " " +
            "&" +
            " " +
            this.aiSelectedFeatureX.name +
            " " +
            "&" +
            " " +
            this.aiSelectedFeatureY.name,
          dragmode: "lasso",
          autosize: true,
          xaxis: {
            zeroline: false,
            automargin: true,
            title: this.aiSelectedFeatureX.name,
          },
          yaxis: { title: this.aiSelectedFeatureY.name, automargin: true },
        };
        Plotly.newPlot("AICluster", data, layout, this.clusterConfig);
        var graphDiv = document.getElementById("AICluster");
        graphDiv.on("plotly_selected", this.ClusterCallBack, false);
        graphDiv.on("plotly_click", this.ClusterShowImg, false);
      });
    },
    // Prepare data for analyse Machine Learning supported Gating
    ClusterCallBack(eventData) {
      var Index0 = [];
      var Index1 = [];
      var Index2 = [];
      var Index3 = [];
      for (var i = 0; i < eventData.points.length; i++) {
        if (eventData.points[i].curveNumber == 0) {
          Index0.push(eventData.points[i].pointIndex);
        } else if (eventData.points[i].curveNumber == 1) {
          Index1.push(eventData.points[i].pointIndex);
        } else if (eventData.points[i].curveNumber == 2) {
          Index2.push(eventData.points[i].pointIndex);
        } else if (eventData.points[i].curveNumber == 3) {
          Index3.push(eventData.points[i].pointIndex);
        }
      }
      for (var i1 = 0; i1 < 4; i1++) {
        this.cluster0.pop();
        this.cluster1.pop();
        this.cluster2.pop();
        this.cluster3.pop();
      }
      for (var i2 = 0; i2 < 4; i2++) {
        this.cgAS.getClusterImg(Index0[i2]).then((info) => {
          this.cluster0.push(info);
        });
        this.cgAS.getClusterImg(Index1[i2]).then((info) => {
          this.cluster1.push(info);
        });
        this.cgAS.getClusterImg(Index2[i2]).then((info) => {
          this.cluster2.push(info);
        });
        this.cgAS.getClusterImg(Index3[i2]).then((info) => {
          this.cluster3.push(info);
        });
      }
      var allLabels = ["Cluster0", "Cluster1", "Cluster2", "Cluster3"];
      var allValues = [
        Index0.length,
        Index1.length,
        Index2.length,
        Index3.length,
      ];
      var ultimateColors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"];
      var data = [
        {
          x: allLabels,
          y: allValues,
          type: "bar",
          marker: { color: ultimateColors },
        },
      ];
      var layoutbar = {
        autosize: true,
        width: 400,
        height: 400,
        xaxis: { title: "Types" },
        yaxis: { title: "Number" },
        title: "Types & Number of selected area",
      };
      Plotly.newPlot("BarChartAI", data, layoutbar, {
        editable: true,
        displaylogo: false,
        modeBarButtonsToRemove: this.config.modeBarButtonsToRemove,
      });
      var piedata = [
        {
          values: allValues,
          labels: allLabels,
          type: "pie",
          marker: { colors: ultimateColors },
        },
      ];
      var layoutpie = {
        autosize: true,
        width: 400,
        height: 400,
        title: "Types & Ratios of selected area",
      };
      Plotly.newPlot("PieChartAI", piedata, layoutpie, {
        editable: true,
        displaylogo: false,
      });
    },
    //Show single Image for Machine Learning supported Gating
    ClusterShowImg(eventData) {
      this.cgAS.getClusterImg(eventData.points[0].pointNumber).then((info) => {
        this.ClickImg = info;
        this.particularScatterCellVisible = true;
      });
    },
    defaultManualImages() {
      var Index0 = [0, 1, 2, 3];
      var Index1 = [0, 1, 2, 3];
      var Index2 = [0, 1, 2, 3];
      var Index3 = [0, 1, 2, 3];
      for (var i2 = 0; i2 < 4; i2++) {
        this.cgAS.getImgs("lym", Index0[i2]).then((info) => {
          this.LymImgs.push(info);
        });
        this.cgAS.getImgs("mon", Index1[i2]).then((info) => {
          this.MonImgs.push(info);
        });
        this.cgAS.getImgs("eos", Index2[i2]).then((info) => {
          this.EosImgs.push(info);
        });
        this.cgAS.getImgs("neu", Index3[i2]).then((info) => {
          this.NeuImgs.push(info);
        });
      }
    },
    defaultAiImages() {
      var Index0 = [0, 1, 2, 3];
      var Index1 = [0, 1, 2, 3].map((x) => x + 78);
      var Index2 = [0, 1, 2, 3].map((x) => x + 137);
      var Index3 = [0, 1, 2, 3].map((x) => x + 179);
      for (var i2 = 0; i2 < 4; i2++) {
        this.cgAS.getClusterImg(Index0[i2]).then((info) => {
          this.cluster0.push(info);
        });
        this.cgAS.getClusterImg(Index1[i2]).then((info) => {
          this.cluster1.push(info);
        });
        this.cgAS.getClusterImg(Index2[i2]).then((info) => {
          this.cluster2.push(info);
        });
        this.cgAS.getClusterImg(Index3[i2]).then((info) => {
          this.cluster3.push(info);
        });
      }
      var allLabels = ["Cluster0", "Cluster1", "Cluster2", "Cluster3"];
      var allValues = [78, 59, 42, 269];
      var ultimateColors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"];
      var data = [
        {
          x: allLabels,
          y: allValues,
          type: "bar",
          marker: { color: ultimateColors },
        },
      ];
      var layoutbar = {
        autosize: true,
        width: 400,
        height: 400,
        xaxis: { title: "Types" },
        yaxis: { title: "Number" },
        title: "Types & Number of selected area",
      };
      Plotly.newPlot("BarChartAI", data, layoutbar, {
        editable: true,
        displaylogo: false,
        modeBarButtonsToRemove: this.config.modeBarButtonsToRemove,
      });
      var piedata = [
        {
          values: allValues,
          labels: allLabels,
          type: "pie",
          marker: { colors: ultimateColors },
        },
      ];
      var layoutpie = {
        autosize: true,
        width: 400,
        height: 400,
        title: "Types & Ratios of selected area",
      };
      Plotly.newPlot("PieChartAI", piedata, layoutpie, {
        editable: true,
        displaylogo: false,
      });
    },
  },
  mounted() {
    this.CellType();
    this.ScatterPlot("dissimilarity", "correlation");
    this.defaultManualImages();
    this.Cluster("meanshift", "dissimilarity", "correlation");
    this.defaultAiImages();
  },
};
</script>
<style scoped>
body {
  font-family: Roboto, sans-serif;
}

.main-card {
  width: 98%;
  margin: 0 auto;
  margin-bottom: 0.5rem;
  border-radius: 3px;
  box-shadow: 0 2px 1px -1px rgba(0, 0, 0, 0.2), 0 1px 1px 0 rgba(0, 0, 0, 0.14),
    0 1px 3px 0 rgba(0, 0, 0, 0.12);
  padding: 25px;
}

.cell-image {
  max-width: 100%;
  max-height: 100%;
}
.image-wrapper-carousel {
  float: left;
  display: inline;
  padding-left: 5px;
  padding-right: 5px;
  height: 100px;
}
.control-row {
}

.axisdropdown {
  width: 13em;
  max-height: 35px;
  vertical-align: middle;
}

.algodropdown {
  width: 11.4em;
  max-height: 35px;
  vertical-align: middle;
}
.v-text-field {
  font-size: 1em;
}
.toolbar {
  height: 80px;
}
</style>
