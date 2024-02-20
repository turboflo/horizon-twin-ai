from horizon_twin_result import HorizonTwinResult
from project import Project
from comparison import Comparison


def search_and_compare(project_description: str, top_k: int = 5) -> list[HorizonTwinResult]:
    project = Project(
        id="mock_id",
        score=0.756342947,
        values=None,
        title="ECOLOOP",
        objective="ECOLOOP project develops and demonstrates a set of solutions to optimise the combination of different energy distributed sources (biogas, biomass, agri-PV, geothermal), meeting the local needs for electricity, heating, cooling, transport and waste and land management in rural areas, fostering regional development and creating benefits for farmers and foresters. The project solutions will focus on promoting the reduction of carbon footprint in rural areas by means of the higher penetration of distributed renewable energy sources, self-consumption and an optimal agricultural/forest waste management, while creating positive effects in biodiversity and soil health and reducing the risk on groundwater contamination. Following this approach, ECOLOOP objectives are:•To optimise the production of biogas from agriculture and forestry wastes in situ. •To combine in an efficient and sustainable way different distributed renewable energy sources (biogas, biomass, agri-PV, geothermal), meeting the local needs for electricity, heating, cooling, transport and waste and land management in rural areas.•To develop innovative renewable-based agricultural protocols and advance bioproducts to increase sustainability and circularity while creating positive effects on biodiversity and soil health and groundwater pollution.•To foster regional development in rural areas.ECOLOOP project will move towards a circular economy in rural areas, focusing on agriculture and forestry sectors, contributing to job creation, gender equality, biodiversity and climate resilience and adaptation. All the benefits provided by ECOLOOP solutions will be demonstrated in 4 pilot sites in Spain, Estonia, Bulgaria and Slovenia, involving different forest and agriculture natural conditions (climate, soils), size and types of crops trees, management techniques, degree of mechanisation, geographic location and socio-economic factors, and considering the interaction of different types of energy sources.",
    )
    comparison = Comparison(
        summary="The ECOLOOP project aims to optimize the combination of different energy distributed sources in rural areas to promote renewable energy usage and regional development.",
        similarity="Both the ECOLOOP project and your idea focus on developing innovative and sustainable approaches for the production of renewable energy sources, with an emphasis on supporting environmental objectives and rural communities.",
        difference="The ECOLOOP project specifically targets optimizing the production of biogas from agriculture and forestry waste, while your idea emphasizes supporting the European Green Deal's objectives and enhancing biodiversity.",
        score=75,
        reason="The similarity score is high because both projects share a common goal of promoting renewable energy sources and sustainability, albeit with slightly different emphases on specific aspects.",
    )
    mock_result = HorizonTwinResult(
        input=project_description,
        project=project,
        comparison=comparison,
    )
    return [mock_result] * top_k
