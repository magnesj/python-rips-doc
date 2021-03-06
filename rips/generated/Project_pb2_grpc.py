# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import Case_pb2 as Case__pb2
import Definitions_pb2 as Definitions__pb2
import PdmObject_pb2 as PdmObject__pb2


class ProjectStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetCurrentCase = channel.unary_unary(
        '/rips.Project/GetCurrentCase',
        request_serializer=Definitions__pb2.Empty.SerializeToString,
        response_deserializer=Case__pb2.CaseRequest.FromString,
        )
    self.GetSelectedCases = channel.unary_unary(
        '/rips.Project/GetSelectedCases',
        request_serializer=Definitions__pb2.Empty.SerializeToString,
        response_deserializer=Case__pb2.CaseInfoArray.FromString,
        )
    self.GetAllCaseGroups = channel.unary_unary(
        '/rips.Project/GetAllCaseGroups',
        request_serializer=Definitions__pb2.Empty.SerializeToString,
        response_deserializer=Case__pb2.CaseGroups.FromString,
        )
    self.GetAllCases = channel.unary_unary(
        '/rips.Project/GetAllCases',
        request_serializer=Definitions__pb2.Empty.SerializeToString,
        response_deserializer=Case__pb2.CaseInfoArray.FromString,
        )
    self.GetCasesInGroup = channel.unary_unary(
        '/rips.Project/GetCasesInGroup',
        request_serializer=Case__pb2.CaseGroup.SerializeToString,
        response_deserializer=Case__pb2.CaseInfoArray.FromString,
        )
    self.GetPdmObject = channel.unary_unary(
        '/rips.Project/GetPdmObject',
        request_serializer=Definitions__pb2.Empty.SerializeToString,
        response_deserializer=PdmObject__pb2.PdmObject.FromString,
        )


class ProjectServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetCurrentCase(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetSelectedCases(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetAllCaseGroups(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetAllCases(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetCasesInGroup(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetPdmObject(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ProjectServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetCurrentCase': grpc.unary_unary_rpc_method_handler(
          servicer.GetCurrentCase,
          request_deserializer=Definitions__pb2.Empty.FromString,
          response_serializer=Case__pb2.CaseRequest.SerializeToString,
      ),
      'GetSelectedCases': grpc.unary_unary_rpc_method_handler(
          servicer.GetSelectedCases,
          request_deserializer=Definitions__pb2.Empty.FromString,
          response_serializer=Case__pb2.CaseInfoArray.SerializeToString,
      ),
      'GetAllCaseGroups': grpc.unary_unary_rpc_method_handler(
          servicer.GetAllCaseGroups,
          request_deserializer=Definitions__pb2.Empty.FromString,
          response_serializer=Case__pb2.CaseGroups.SerializeToString,
      ),
      'GetAllCases': grpc.unary_unary_rpc_method_handler(
          servicer.GetAllCases,
          request_deserializer=Definitions__pb2.Empty.FromString,
          response_serializer=Case__pb2.CaseInfoArray.SerializeToString,
      ),
      'GetCasesInGroup': grpc.unary_unary_rpc_method_handler(
          servicer.GetCasesInGroup,
          request_deserializer=Case__pb2.CaseGroup.FromString,
          response_serializer=Case__pb2.CaseInfoArray.SerializeToString,
      ),
      'GetPdmObject': grpc.unary_unary_rpc_method_handler(
          servicer.GetPdmObject,
          request_deserializer=Definitions__pb2.Empty.FromString,
          response_serializer=PdmObject__pb2.PdmObject.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'rips.Project', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
