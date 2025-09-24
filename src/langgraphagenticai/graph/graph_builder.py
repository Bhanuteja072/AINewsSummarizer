from langgraph.graph import StateGraph
from langgraph.prebuilt import tools_condition
from langgraph.graph import START,END
from src.langgraphagenticai.state.state import State
from src.langgraphagenticai.tools.search_tool import get_tools,create_tool_node
from src.langgraphagenticai.nodes.ai_news_node import AINewsNode


class GraphBuilder:
    def __init__(self,model):
        self.llm=model
        self.graph_builder=StateGraph(State)

   

   

    def ai_news_builder_graph(self):

        ai_news_node=AINewsNode(self.llm)

        ## added the nodes

        self.graph_builder.add_node("fetch_news",ai_news_node.fetch_news)
        self.graph_builder.add_node("summarize_news",ai_news_node.summarize_news)
        self.graph_builder.add_node("save_result",ai_news_node.save_result)

        #added the edges

        self.graph_builder.set_entry_point("fetch_news")
        self.graph_builder.add_edge("fetch_news","summarize_news")
        self.graph_builder.add_edge("summarize_news","save_result")
        self.graph_builder.add_edge("save_result", END)


       



    def setup_graph(self, usecase: str):
        """
        Sets up the graph for the selected use case.
        """
        if usecase == "AI News":
            self.ai_news_builder_graph()

        return self.graph_builder.compile()
