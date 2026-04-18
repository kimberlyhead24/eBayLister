# All Open Tasks

## Project Setup and Agile Planning
- [x] Define updated project scope based on the real seller workflow. ✅ 2026-04-14
- [ ] Write problem statement for AI class project.
- [ ] Write success criteria for MVP.
- [ ] Decide what will be AI, what will be rule-based, and what will stay manual.
- [x] Update project timeline in Microsoft Project to match the new application plan. ✅ 2026-04-14
- [ ] Record why the app no longer focuses on image cleanup and instead focuses on classification, pricing, and workflow automation.

## MVP Foundation
- [x] Define MVP definition and Agile backlog. ✅ 2026-04-17
- [x] Confirm seller workflow: photo → classify → draft → review → publish. ✅ 2026-04-17
- [x] Create basic project structure and delivery plan. ✅ 2026-04-17
- [x] Set up draft storage and model using JSON. ✅ 2026-04-18
- [ ] Implement basic UI for photo upload and draft review.
- [x] Add listing status flow: draft, needs review, approved, published, failed. ✅ 2026-04-18
- [ ] Add seller notes field and business-review fields to the draft model.
- [ ] Add audit history fields for created by, reviewed by, and approved by.

## Item Classification and Recognition
- [ ] Research and choose product classification approach for listing photos.
- [ ] Define structured classification output: item name, brand, category, model, condition clues.
- [ ] Build first-pass item classification pipeline from uploaded photo.
- [ ] Research condition-detection options.
- [ ] Implement category and condition suggestion logic.
- [ ] Test classification on real seller photos from the current workflow.
- [ ] Measure classification accuracy on sample items.
- [ ] Add fallback manual correction flow for low-confidence predictions.
- [ ] Create note documenting how classification output feeds the search and pricing pipeline.

## AI Bot and Knowledge System
- [ ] Define local AI bot architecture for the class project.
- [ ] Decide what uses RAG and what uses rule-based logic.
- [ ] Build seller workflow knowledge base.
- [ ] Build eBay-specific listing knowledge base.
- [ ] Store examples of good listing titles, descriptions, disclaimers, and item specifics.
- [ ] Create prompt templates for title generation.
- [ ] Create prompt templates for description generation.
- [ ] Create prompt templates for disclaimer and policy text generation.
- [ ] Link retrieved knowledge to draft generation.
- [ ] Add source-aware output so the bot can explain where guidance came from.
- [ ] Document why RAG is being used before fine-tuning. RAG is typically better for dynamic, frequently updated knowledge, while fine-tuning is more expensive and harder to update quickly. [web:452][web:397][web:449]

## Live Market Data and Pricing Logic
- [ ] Research eBay Browse API for current listing search.
- [ ] Build search query generator from classified item name, brand, category, and condition.
- [ ] Pull current active listing data from eBay.
- [ ] Normalize listing prices, shipping, and condition data into comparable comps.
- [ ] Research how sold-comparison data will be gathered or approximated.
- [ ] Add outlier filtering for unrealistic listing prices.
- [ ] Define pricing inputs: MSRP, active comps, sold comps, fees, shipping, condition, and cost basis.
- [ ] Implement pricing suggestion logic: quick sale, market price, high-price.
- [ ] Add minimum-profit floor logic so listings do not lose money.
- [ ] Add competition-adjustment rule for slight undercutting when profitable.
- [ ] Add fallback pricing logic when no reliable comps are found.
- [ ] Output explanation text showing why each price recommendation was chosen.
- [ ] Document why live market data is needed in addition to the internal knowledge base. The eBay Browse API supports current item searches by keyword, category, and other criteria, which makes it useful for current pricing context. [web:419][web:418]

## Listing Generation Logic
- [ ] Finalize structure of title templates.
- [ ] Finalize structure of description templates.
- [ ] Implement item specifics generation logic.
- [ ] Implement condition-summary generation logic.
- [ ] Implement disclaimer generation logic.
- [ ] Implement seller-policy note generation logic.
- [ ] Persist generated title, description, condition, disclaimers, and pricing back into the draft model.
- [ ] Add manual review requirement before publish.
- [ ] Save AI-generated output separately from final edited output for comparison.

## Workflow Rules from Seller Training
- [ ] Add Google Lens or image-identification step to workflow intake.
- [ ] Add similar-listing lookup step.
- [ ] Add “make similar listing” decision flow.
- [ ] Add title-writing step before final description cleanup.
- [ ] Add condition-writing step.
- [ ] Add disclaimers step.
- [ ] Add selling-policies note step.
- [ ] Add UPC and item-specifics step.
- [ ] Add category/store-type selection step.
- [ ] Add pricing decision step using current listings, sold data, and MSRP anchor.
- [ ] Add auction decision step for high-value items.
- [ ] Add quantity rule for duplicate items where allowed.
- [ ] Add allow-offers default rule unless overridden.
- [ ] Add shipping decision rule: USPS default, FedEx for larger items.
- [ ] Add post-publish sharing step for Facebook and other product owners.

## eBay Integration and Finalization
- [ ] Confirm eBay developer sandbox account setup.
- [ ] Add placeholder config values for AUTH_EBAY, KEY_EBAY, EBAY_APP_ID, and related settings.
- [ ] Create eBay inventory location via sandbox.
- [ ] Research required business policies for payment, returns, and shipping.
- [ ] Implement inventory item creation using createOrReplaceInventoryItem.
- [ ] Implement offer creation using createOffer.
- [ ] Implement publishOffer workflow.
- [ ] Handle validation and publish errors.
- [ ] Connect approved draft flow to eBay publish flow.
- [ ] Run full end-to-end sandbox test: photo → classify → draft → approve → publish.
- [ ] Finalize documentation and prepare submission materials.

## Cross-Device UI
- [ ] Keep the application web-based so it works on Android, iPhone, and desktop browsers.
- [ ] Design upload page for phone-sized screens first.
- [ ] Design draft review page for mobile editing.
- [ ] Add status badges for draft, review, approved, published, and failed.
- [ ] Add listing summary card with image preview and AI suggestions.

## Testing and Evaluation
- [ ] Create evaluation set of real sample items from the seller workflow.
- [ ] Test classification accuracy.
- [ ] Test title quality against manual seller-created titles.
- [ ] Test description quality against manual seller-created descriptions.
- [ ] Test pricing recommendations against real listing choices.
- [ ] Record where AI helps, where rules help, and where humans still need to decide.
- [ ] Document failure cases and fallback flows.
- [ ] Save screenshots and notes for final portfolio and class presentation.

## Research and Portfolio Documentation
- [ ] Record daily research notes in Obsidian.
- [ ] Document how live seller training changed the application architecture.
- [ ] Document current-state workflow.
- [ ] Document future-state workflow.
- [ ] Add Mermaid diagram for current seller workflow.
- [ ] Add Mermaid diagram for future app workflow.
- [ ] Write portfolio note explaining the project as AI engineering, workflow automation, and marketplace integration.
- [ ] Prepare resume bullets based on workflow discovery, AI design, pricing logic, and eBay integration.